+++
title = "Practica 3.11 - Invasion Alienigena VI: Haciendo que la Flota se Mueva"
author = ["Jordi"]
tags = ["prácticas"]
url = "/pygame6/"
draft = true
+++

## Objetivo {#objetivo}

Tu flota de alienigenas esta en pantalla... pero no se mueve. En esta practica vas a darle vida: la flota se desplazara lateralmente, bajara un escalon al tocar un borde, y tus balas podran destruir alienigenas. Cuando la flota quede vacia, aparecera una nueva oleada.

Vas a aprender a:

-   Mover un grupo de sprites de forma coordinada
-   Usar una variable de direccion (`1` / `-1`) para invertir el sentido del movimiento
-   Detectar colisiones entre dos grupos de sprites (`groupcollide`)
-   Regenerar contenido dinamicamente (nueva flota al limpiar la anterior)
-   Refactorizar: extraer logica compleja a metodos privados

Al terminar, tu juego tendra alienigenas que se mueven, bajan, y se destruyen cuando les disparas. Empieza a parecerse a un juego de verdad.

> Basado en el Capitulo 13 del libro _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Punto de partida {#punto-de-partida}

Tu P3.10 funcional: una nave que dispara balas y una flota estatica de alienigenas.

```text
PRACTICA3.11/
+-- invasion_alienigena.py   <-- tu P3.10 (vas a ampliar)
+-- ajustes.py               <-- tu P3.10 (vas a ampliar)
+-- nave.py                  <-- tu P3.10 (sin cambios)
+-- bala.py                  <-- tu P3.10 (sin cambios)
+-- alienigena.py            <-- tu P3.10 (vas a ampliar)
+-- images/
    +-- nave.bmp
    +-- alienigena.bmp
```

No necesitas ficheros nuevos. Todo el trabajo es ampliar los ficheros existentes.

---


## Paso 1 -- Mover los alienigenas {#paso-1-mover-los-alienigenas}

Los alienigenas necesitan moverse. Añade la velocidad en `ajustes.py`:

```python
# Ajustes de alienigenas
self.velocidad_alienigena = 1.0
```

Ahora dale al alienigena la capacidad de moverse. En `alienigena.py`, guarda una referencia a los ajustes y añade un metodo `actualizar()`:

```python
def __init__(self, ia_juego):
    """Inicializa el alienigena y su posicion de partida."""
    super().__init__()
    self.pantalla = ia_juego.pantalla
    self.ajustes = ia_juego.ajustes

    # Cargar imagen y obtener su rect
    self.imagen = pygame.image.load('images/alienigena.bmp')
    self.rect = self.imagen.get_rect()

    # Colocar cerca de la esquina superior izquierda
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    # Guardar posicion horizontal como float
    self.x = float(self.rect.x)

def actualizar(self):
    """Mueve el alienigena lateralmente."""
    self.x += self.ajustes.velocidad_alienigena * self.ajustes.direccion_flota
    self.rect.x = self.x
```

¿Que hace `actualizar()`? Desplaza la posicion horizontal del alienigena. La direccion depende de `direccion_flota`: si vale `1`, se mueve a la derecha; si vale `-1`, a la izquierda. El truco es que **todos** los alienigenas comparten los mismos ajustes, asi que toda la flota se mueve a la vez.

---


## Paso 2 -- Detectar los bordes de la pantalla {#paso-2-detectar-los-bordes-de-la-pantalla}

Antes de que la flota se mueva de verdad, necesitamos que los alienigenas sepan cuando han llegado al borde de la pantalla.

Añade este metodo a la clase `Alienigena`:

```python
def verificar_bordes(self):
    """Devuelve True si el alienigena esta en un borde de la pantalla."""
    pantalla_rect = self.pantalla.get_rect()
    return (self.rect.right >= pantalla_rect.right) or (self.rect.left <= 0)
```

Cada alienigena puede comprobar si su borde derecho ha llegado al borde derecho de la pantalla, o si su borde izquierdo ha llegado a 0. Devuelve `True` en cualquiera de los dos casos.

---


## Paso 3 -- Cambiar direccion y bajar {#paso-3-cambiar-direccion-y-bajar}

Ahora necesitas dos ajustes nuevos en `ajustes.py`:

```python
# Ajustes de alienigenas
self.velocidad_alienigena = 1.0
self.velocidad_caida_flota = 10
self.direccion_flota = 1  # 1 = derecha, -1 = izquierda
```

Y dos metodos nuevos en `InvasionAlienigena`:

```python
def _verificar_bordes_flota(self):
    """Responde si algun alienigena ha llegado a un borde."""
    for alienigena in self.alienigenas.sprites():
        if alienigena.verificar_bordes():
            self._cambiar_direccion_flota()
            break

def _cambiar_direccion_flota(self):
    """Baja toda la flota y cambia su direccion."""
    for alienigena in self.alienigenas.sprites():
        alienigena.rect.y += self.ajustes.velocidad_caida_flota
    self.ajustes.direccion_flota *= -1
```

La logica es sencilla:

-   `_verificar_bordes_flota()` recorre todos los alienigenas. Si **alguno** toca un borde, invoca `_cambiar_direccion_flota()` y sale del bucle con `break`.
-   `_cambiar_direccion_flota()` baja **todos** los alienigenas (sumando `velocidad_caida_flota` a su Y) e invierte la direccion multiplicando por `-1`.

El `break` es importante: sin el, si varios alienigenas tocan el borde a la vez, la direccion se invertiria multiples veces en el mismo frame.

---


## Paso 4 -- Refactorizar: `_actualizar_alienigenas()` {#paso-4-refactorizar-actualizar-alienigenas}

Antes de añadir mas logica al bucle principal, es buen momento para agrupar la actualizacion de alienigenas en su propio metodo privado:

```python
def _actualizar_alienigenas(self):
    """Verifica bordes y actualiza posiciones de toda la flota."""
    self._verificar_bordes_flota()
    self.alienigenas.update()
```

Ahora tu bucle principal (`ejecutar_juego()`) queda mas limpio. Donde antes llamabas a `self.alienigenas.update()`, sustituye por:

```python
self._actualizar_alienigenas()
```

Ejecuta el juego. La flota deberia moverse a la derecha, bajar un escalon al tocar el borde derecho, moverse a la izquierda, bajar al tocar el borde izquierdo, y asi sucesivamente.

---


## Paso 5 -- Disparar alienigenas {#paso-5-disparar-alienigenas}

Tus balas atraviesan la flota sin hacer nada. Vamos a arreglar eso.

En `_actualizar_balas()` (el metodo donde ya eliminas las balas que salen de pantalla), añade la deteccion de colisiones:

```python
def _actualizar_balas(self):
    """Actualiza la posicion de las balas y elimina las antiguas."""
    self.balas.update()

    # Eliminar balas que han salido de pantalla
    for bala in self.balas.copy():
        if bala.rect.bottom <= 0:
            self.balas.remove(bala)

    self._verificar_colisiones_bala_alienigena()
```

Y el metodo de colisiones:

```python
def _verificar_colisiones_bala_alienigena(self):
    """Detecta colisiones entre balas y alienigenas."""
    # Eliminar balas y alienigenas que han colisionado
    colisiones = pygame.sprite.groupcollide(
        self.balas, self.alienigenas, True, True)
```

`groupcollide()` compara cada sprite de un grupo con cada sprite del otro. Los dos `True` significan:

-   Primer `True`: eliminar la bala que colisiona
-   Segundo `True`: eliminar el alienigena que colisiona

Asi, cuando una bala toca un alienigena, ambos desaparecen.

Ejecuta el juego y dispara. Los alienigenas deberian desaparecer al ser alcanzados.

---


## Paso 6 -- Regenerar la flota {#paso-6-regenerar-la-flota}

Si destruyes todos los alienigenas... ¿que pasa? Nada. La pantalla queda vacia. Vamos a crear una nueva oleada cada vez que la flota sea eliminada.

Añade esta logica al final de `_verificar_colisiones_bala_alienigena()`:

```python
def _verificar_colisiones_bala_alienigena(self):
    """Detecta colisiones entre balas y alienigenas."""
    colisiones = pygame.sprite.groupcollide(
        self.balas, self.alienigenas, True, True)

    if not self.alienigenas:
        # Destruir balas existentes y crear nueva flota
        self.balas.empty()
        self._crear_flota()
```

`if not self.alienigenas` es `True` cuando el grupo esta vacio (Python trata los contenedores vacios como `False`). En ese caso:

1.  `self.balas.empty()` elimina todas las balas que quedaran en pantalla
2.  `self._crear_flota()` genera una flota nueva desde cero

Ejecuta el juego, destruye toda la flota, y comprueba que aparece una nueva.

---


## Entrega {#entrega}

-   [ ] `alienigena.py` -- `actualizar()` mueve lateralmente, `verificar_bordes()` detecta bordes
-   [ ] `ajustes.py` -- `velocidad_alienigena`, `velocidad_caida_flota`, `direccion_flota`
-   [ ] `invasion_alienigena.py` -- `_actualizar_alienigenas()`, `_verificar_bordes_flota()`, `_cambiar_direccion_flota()`, colisiones con `groupcollide`, regenerar flota
-   [ ] La flota se mueve lateralmente y baja al tocar un borde
-   [ ] Las balas destruyen alienigenas
-   [ ] Al eliminar toda la flota, aparece una nueva oleada
-   [ ] La nave y las balas siguen funcionando correctamente

&gt;    RECORDATORIO: organiza las entregas por carpetas (P3.6 a P3.11)

---


## BONUS -- Para nota maxima {#bonus-para-nota-maxima}

| **Bonus**                      | **Descripcion**                                                     | **Puntos** |
|--------------------------------|---------------------------------------------------------------------|------------|
| Velocidad progresiva           | La flota se mueve mas rapido con cada oleada nueva                  | **+0.75**  |
| Contador de puntos en terminal | Imprimir puntos en consola al destruir un alienigena                | **+0.5**   |
| Sonido al impactar             | Reproducir un sonido cuando una bala destruye un alienigena         | **+0.75**  |
| Explosion visual               | Mostrar brevemente un sprite de explosion al destruir un alienigena | **+1**     |
| Oleadas con mas filas          | Cada nueva flota tiene una fila mas que la anterior                 | **+0.5**   |
| Gotas de lluvia (13-3)         | Crear una cuadricula de gotas que cae hasta desaparecer abajo       | **+1**     |
| Lluvia continua (13-4)         | Al desaparecer una fila de gotas, aparece una nueva arriba          | **+0.75**  |

> Los ejercicios 13-3 y 13-4 son los _TRY IT YOURSELF_ del libro. Intentarlos es la mejor forma de consolidar lo aprendido.

<!--quoteend-->

> En las siguientes Practicas los alienigenas podran destruir tu nave y el juego tendra vidas, "Game Over!", y boton de reinicio. La flota ya no sera solo decorativa.

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                        | **Donde lo ves**                                                                       |
|-------------------------------------|----------------------------------------------------------------------------------------|
| **Variable de direccion**           | `direccion_flota` (1/-1) multiplicada por velocidad invierte el sentido                |
| **Deteccion de bordes**             | `verificar_bordes()` compara `rect.right/left` con bordes de pantalla                  |
| **Patron verificar-y-actuar**       | `_verificar_bordes_flota()` recorre, detecta, y delega en `_cambiar_direccion_flota()` |
| **groupcollide()**                  | Compara dos grupos sprite a sprite y elimina los que colisionan                        |
| **Regeneracion de contenido**       | `if not grupo:` detecta grupo vacio y dispara `_crear_flota()`                         |
| **Refactorizacion: metodo privado** | `_actualizar_alienigenas()` agrupa logica para mantener el bucle limpio                |

---


## Rubrica {#rubrica}

| **Criterio**                                                   | **Puntos** |
|----------------------------------------------------------------|------------|
| `alienigena.py` -- `actualizar()` + `verificar_bordes()`       | 3          |
| `invasion_alienigena.py` -- direccion, bordes, colisiones      | 3          |
| `ajustes.py` -- velocidad + direccion + caida                  | 1          |
| Colisiones bala-alienigena funcionan                           | 1          |
| Ejecucion (flota se mueve, baja, aliens destruibles, regenera) | 2          |
| **Total base**                                                 | **10**     |
| BONUS (hasta +5.25, max 10)                                    | +5.25      |

---

> _"La primera vez que destruyes un alienigena y aparece otra oleada, entiendes el bucle infinito del game design: destruir, crear, repetir."_
