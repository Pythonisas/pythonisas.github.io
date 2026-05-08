+++
title = "Practica 3.9 - Invasion Alienigena IV: Disparando Balas"
author = ["Jordi"]
publishDate = 2026-05-01
tags = ["prácticas"]
url = "/pygame4/"
draft = false
+++

## Objetivo {#objetivo}

Tu nave se mueve, pero esta indefensa. En esta practica le vas a dar armas: al pulsar la barra espaciadora, la nave disparara balas que suben por la pantalla.

Parece sencillo, pero detras de cada disparo hay varios conceptos nuevos:

-   Crear objetos **sobre la marcha** (cada bala es una instancia nueva)
-   Agruparlos con `pygame.sprite.Group` para gestionarlos en bloque
-   Dibujar rectangulos sin imagen (`pygame.draw.rect`)
-   Eliminar objetos que ya no sirven (limpieza de memoria)
-   Limitar recursos del jugador (maximo de balas en pantalla)

Al terminar seras capaz de:

-   Crear una clase `Bala` que hereda de `Sprite`
-   Construir un `rect` desde cero (sin imagen)
-   Gestionar colecciones de sprites con `Group`
-   Limpiar objetos fuera de pantalla para no desperdiciar memoria
-   Refactorizar el game loop en metodos privados cada vez mas limpios

> Basado en el Capitulo 12 de _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Punto de partida {#punto-de-partida}

Tu P3.8 funcional: una nave que se mueve con las flechas, con eventos gestionados en `_verificar_eventos()`.

```text
PRACTICA3.9/
+-- invasion_alienigena.py   <-- tu P3.8 (vas a ampliar)
+-- ajustes.py               <-- tu P3.8 (vas a añadir ajustes de bala)
+-- nave.py                  <-- tu P3.8 (sin cambios)
+-- bala.py                  <-- NUEVO fichero
+-- images/
    +-- nave.bmp
```

---


## Paso 1 -- Ajustes de la bala en `Ajustes` {#paso-1-ajustes-de-la-bala-en-ajustes}

Antes de crear la clase `Bala`, necesitas saber como sera: velocidad, tamaño y color. Centraliza estos valores en `ajustes.py`, igual que hiciste con `velocidad_nave`:

```python
# Ajustes de bala
self.velocidad_bala = 2.0
self.ancho_bala = 3
self.alto_bala = 15
self.color_bala = (60, 60, 60)
```

Esto produce balas grises de 3x15 pixeles que viajan un poco mas rapido que la nave. Al tenerlos en `Ajustes`, puedes cambiar el aspecto de las balas sin tocar la logica del juego.

---


## Paso 2 -- Crear la clase `Bala` {#paso-2-crear-la-clase-bala}

Crea un nuevo fichero `bala.py`. La bala no tiene imagen — es un rectangulo que fabricamos desde cero con `pygame.Rect()`.


### 2.1 ¿Que es un Sprite? {#2-dot-1-que-es-un-sprite}

Hasta ahora, tus objetos (`Nave`, `Ajustes`) eran clases normales. La bala sera diferente: hereda de `pygame.sprite.Sprite`. Un sprite es un objeto visual que Pygame sabe agrupar, actualizar y dibujar en bloque. Cuando tienes 10 balas en pantalla, no quieres llamar a `actualizar()` una por una — quieres decir "actualiza todas" y que Pygame lo haga por ti.


### 2.2 El constructor {#2-dot-2-el-constructor}

El constructor de `Bala` recibe la instancia del juego (`ia_juego`) para acceder a la pantalla, los ajustes y la posicion de la nave:

```python
import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Gestiona las balas disparadas por la nave."""

    def __init__(self, ia_juego):
        """Crea una bala en la posicion actual de la nave."""
        super().__init__()
        self.pantalla = ia_juego.pantalla
        self.ajustes = ia_juego.ajustes
        self.color = self.ajustes.color_bala

        # Crear el rect de la bala en (0,0) y recolocar
        self.rect = pygame.Rect(
            0, 0, self.ajustes.ancho_bala, self.ajustes.alto_bala)
        self.rect.midtop = ia_juego.nave.rect.midtop

        # Posicion como float (mismo patron que la nave)
        self.y = float(self.rect.y)
```

Observa tres cosas:

-   `super().__init__()` — necesario para que `Sprite` funcione
-   `pygame.Rect(0, 0, ancho, alto)` — construye un rectangulo sin imagen. Primero lo creas en el origen y luego lo colocas donde toca
-   `self.rect.midtop = ia_juego.nave.rect.midtop` — la bala aparece en la punta de la nave, como si saliera de ella
-   `self.y = float(...)` — mismo truco que en la nave: guardar la posicion como float para velocidades fraccionarias


### 2.3 El metodo `actualizar()` {#2-dot-3-el-metodo-actualizar}

La bala sube por la pantalla. "Subir" en Pygame significa **reducir** la coordenada Y:

```python
def actualizar(self):
    """Mueve la bala hacia arriba."""
    self.y -= self.ajustes.velocidad_bala
    self.rect.y = self.y
```

Fijate: una vez disparada, la bala nunca cambia su X. Aunque la nave se mueva despues, la bala sigue recta hacia arriba.


### 2.4 El metodo `dibujar_bala()` {#2-dot-4-el-metodo-dibujar-bala}

Como la bala no tiene imagen, no usamos `blit()`. En su lugar, Pygame ofrece `pygame.draw.rect()` para pintar rectangulos solidos:

```python
def dibujar_bala(self):
    """Dibuja la bala en pantalla."""
    pygame.draw.rect(self.pantalla, self.color, self.rect)
```

---


## Paso 3 -- Almacenar las balas en un grupo {#paso-3-almacenar-las-balas-en-un-grupo}

Cada vez que el jugador dispara, nace una nueva bala. Necesitas un sitio donde guardarlas todas. Para eso existe `pygame.sprite.Group`: una coleccion especial para sprites.

En el constructor de `InvasionAlienigena`, crea el grupo:

```python
self.balas = pygame.sprite.Group()
```

Un `Group` funciona como una lista, pero con superpoderes:

-   `self.balas.update()` — llama a `actualizar()` de **cada** bala del grupo automaticamente
-   `self.balas.sprites()` — devuelve la lista de balas para recorrerla
-   `self.balas.add(bala)` — añade un sprite al grupo (como `append` pero para sprites)

---


## Paso 4 -- Disparar con la barra espaciadora {#paso-4-disparar-con-la-barra-espaciadora}


### 4.1 Detectar la tecla {#4-dot-1-detectar-la-tecla}

En `_verificar_eventos()` (o en tu metodo `_verificar_pulsacion_tecla()` si lo extrajiste en P3.8), añade un caso para `pygame.K_SPACE`:

```python
elif evento.key == pygame.K_SPACE:
    self._disparar_bala()
```


### 4.2 El metodo `_disparar_bala()` {#4-dot-2-el-metodo-disparar-bala}

Crea un metodo privado que fabrique una bala y la añada al grupo:

```python
def _disparar_bala(self):
    """Crea una bala nueva y la añade al grupo."""
    nueva_bala = Bala(self)
    self.balas.add(nueva_bala)
```

Cada disparo crea un **objeto nuevo**. Si disparas 5 veces, hay 5 instancias de `Bala` viviendo en el grupo.


### 4.3 Actualizar y dibujar las balas en el game loop {#4-dot-3-actualizar-y-dibujar-las-balas-en-el-game-loop}

En `ejecutar_juego()`, añade la actualizacion de balas despues de la nave. Y en la fase de dibujo, recorre el grupo para pintar cada bala:

```python
# En el game loop:
self.nave.actualizar()
self.balas.update()          # actualiza TODAS las balas de golpe

# En la fase de dibujo (antes de dibujar la nave):
for bala in self.balas.sprites():
    bala.dibujar_bala()
self.nave.dibujarme()
```

Las balas se dibujan **antes** que la nave para que aparezcan por detras, no por encima.

---


## Paso 5 -- Eliminar balas fuera de pantalla {#paso-5-eliminar-balas-fuera-de-pantalla}

Problema: las balas que salen por arriba no desaparecen — solo dejan de verse. Siguen existiendo en memoria, con su coordenada Y cada vez mas negativa. Si no las eliminas, el juego se ralentiza progresivamente.

Solucion: despues de actualizar las balas, revisa cuales han salido de pantalla y eliminelas:

```python
# Eliminar balas que han desaparecido
for bala in self.balas.copy():
    if bala.rect.bottom <= 0:
        self.balas.remove(bala)
```

¿Por que `self.balas.copy()` y no `self.balas` directamente? Porque Python no permite modificar una coleccion mientras la recorres. Al iterar sobre una copia, puedes eliminar elementos del original sin problemas.

`bala.rect.bottom <` 0= significa que el borde inferior de la bala ha cruzado el borde superior de la pantalla — ya no se ve.

---


## Paso 6 -- Limitar el numero de balas {#paso-6-limitar-el-numero-de-balas}

Sin limite, el jugador puede llenar la pantalla de balas mantienendo pulsado ESPACIO. Eso rompe la dificultad del juego. La solucion: un maximo de balas simultaneas.

En `ajustes.py`:

```python
self.balas_permitidas = 3
```

Y modifica `_disparar_bala()` para que compruebe antes de crear:

```python
def _disparar_bala(self):
    """Crea una bala nueva solo si no se ha alcanzado el limite."""
    if len(self.balas) < self.ajustes.balas_permitidas:
        nueva_bala = Bala(self)
        self.balas.add(nueva_bala)
```

Ahora el jugador solo puede tener 3 balas en pantalla. Tiene que apuntar bien y esperar a que una desaparezca antes de disparar otra.

---


## Paso 7 -- Refactorizar: `_actualizar_balas()` {#paso-7-refactorizar-actualizar-balas}

El game loop se ha complicado otra vez. Extrae toda la logica de balas (actualizar posiciones + eliminar viejas) a un metodo privado:

```python
def _actualizar_balas(self):
    """Actualiza la posicion de las balas y elimina las antiguas."""
    self.balas.update()

    for bala in self.balas.copy():
        if bala.rect.bottom <= 0:
            self.balas.remove(bala)
```

El game loop queda asi:

```python
def ejecutar_juego(self):
    while True:
        self._verificar_eventos()
        self.nave.actualizar()
        self._actualizar_balas()

        self.pantalla.fill(self.ajustes.color_fondo)
        for bala in self.balas.sprites():
            bala.dibujar_bala()
        self.nave.dibujarme()
        pygame.display.flip()
        self.clock.tick(60)
```

Cuatro fases claras: eventos, actualizacion, dibujo, tick. Cada una en su sitio.

---


## Entrega {#entrega}

-   [ ] `ajustes.py` -- con ajustes de bala (velocidad, tamaño, color, limite)
-   [ ] `bala.py` -- clase `Bala(Sprite)` con constructor, `actualizar()`, `dibujar_bala()`
-   [ ] `invasion_alienigena.py` -- grupo de balas, `_disparar_bala()`, `_actualizar_balas()`, dibujo de balas
-   [ ] `nave.py` -- sin cambios respecto a P3.8
-   [ ] Al pulsar ESPACIO, la nave dispara balas que suben y desaparecen
-   [ ] Maximo 3 balas en pantalla simultaneamente
-   [ ] Pulsar X o Q cierra el juego

&gt;    RECORDATORIO: organiza las entregas por carpetas (P3.6-Pygame1, P3.7-Pygame2, P3.8-Pygame3, P3.9-Pygame4...)

---


## BONUS -- Para nota maxima {#bonus-para-nota-maxima}

| **Bonus**                    | **Descripcion**                                                  | **Puntos** |
|------------------------------|------------------------------------------------------------------|------------|
| `_actualizar_pantalla()`     | Extraer la fase de dibujo a su propio metodo privado             | **+0.5**   |
| Balas con color configurable | Poder cambiar el color de bala desde `Ajustes` sin tocar `Bala`  | **+0.25**  |
| Sonido de disparo            | Reproducir un efecto de sonido al disparar (`pygame.mixer`)      | **+0.75**  |
| Disparo rapido               | Mantener ESPACIO pulsado dispara automaticamente (con cooldown)  | **+0.75**  |
| Balas laterales              | Ademas de hacia arriba, poder disparar en diagonal o a los lados | **+0.75**  |
| Contador de balas            | Mostrar en pantalla cuantas balas quedan disponibles             | **+0.5**   |

> El bonus de `_actualizar_pantalla()` prepara la P3.10 (aliens). Cada metodo privado que extraigas ahora es una linea menos que mantener cuando el juego crezca.

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                      | **Donde lo ves**                                                  |
|-----------------------------------|-------------------------------------------------------------------|
| **Herencia de Sprite**            | `class Bala(Sprite):` hereda para poder usar `Group`              |
| **pygame.Rect() sin imagen**      | Construir un rectangulo desde cero con coordenadas y dimensiones  |
| **pygame.draw.rect()**            | Dibujar un rectangulo solido en pantalla (sin imagen, solo color) |
| **pygame.sprite.Group**           | Coleccion de sprites: `update()` y `sprites()` en bloque          |
| **Crear objetos sobre la marcha** | Cada ESPACIO crea un `Bala(self)` nuevo — instanciacion dinamica  |
| **Limpieza de memoria**           | Eliminar balas fuera de pantalla con `.copy()` + `.remove()`      |
| **Limitar recursos**              | `balas_permitidas` obliga al jugador a apuntar bien               |
| **Refactorizacion progresiva**    | Extraer `_actualizar_balas()` para mantener el game loop legible  |

---


## Rubrica {#rubrica}

| **Criterio**                                            | **Puntos** |
|---------------------------------------------------------|------------|
| `bala.py` -- clase `Bala(Sprite)` completa              | 3          |
| `invasion_alienigena.py` -- disparar + grupo + limpieza | 3          |
| `ajustes.py` -- ajustes de bala + limite                | 1          |
| Eliminacion de balas fuera de pantalla                  | 1          |
| Ejecucion (disparo funciona, max 3 balas, sin errores)  | 2          |
| **Total base**                                          | **10**     |
| BONUS (hasta +3.5, max 10)                              | +3.5       |

---

> _"Disparar es facil. Lo dificil es saber cuando no disparar."_ -- Cualquier jugador con solo 3 balas
