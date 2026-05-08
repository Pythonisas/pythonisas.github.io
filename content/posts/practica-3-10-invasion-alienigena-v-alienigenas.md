+++
title = "Practica 3.10 - Invasion Alienigena V: Alienigenas!"
author = ["Jordi"]
tags = ["prácticas"]
url = "/pygame5/"
draft = true
+++

## Objetivo {#objetivo}

Tu nave dispara, pero no tiene a quien disparar. En esta practica vas a poblar la pantalla de alienigenas: primero uno solo, luego una fila entera, y finalmente una flota completa que ocupa la mitad superior de la ventana.

Este es un salto de complejidad importante. Vas a aprender a:

-   Crear objetos en masa con bucles anidados
-   Calcular posiciones con aritmetica de rectangulos
-   Usar `pygame.sprite.Group` para gestionar decenas de sprites a la vez
-   Dibujar un grupo entero con una sola llamada (`.draw()`)
-   Refactorizar progresivamente mientras el codigo crece

Al terminar, tu juego mostrara una flota de alienigenas alineados en filas y columnas, listos para la batalla.

> Basado en el Capitulo 13 de _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Punto de partida {#punto-de-partida}

Tu P3.9 funcional: una nave que se mueve y dispara balas.

```text
PRACTICA3.10/
+-- invasion_alienigena.py   <-- tu P3.9 (vas a ampliar)
+-- ajustes.py               <-- tu P3.9 (sin cambios por ahora)
+-- nave.py                  <-- tu P3.9 (sin cambios)
+-- bala.py                  <-- tu P3.9 (sin cambios)
+-- alienigena.py            <-- NUEVO fichero
+-- images/
    +-- nave.bmp
    +-- alienigena.bmp       <-- NUEVA imagen
```

Necesitaras una imagen para el alienigena. Puedes usar la del libro ([recursos PCC](https://ehmatthes.github.io/pcc_3e)) o buscar una propia. Guardala en `images/alienigena.bmp`.

---


## Paso 1 -- Crear la clase `Alienigena` {#paso-1-crear-la-clase-alienigena}

El alienigena es muy parecido a la nave: un sprite con imagen que se coloca en pantalla. Crea `alienigena.py`:

```python
import pygame
from pygame.sprite import Sprite

class Alienigena(Sprite):
    """Representa un alienigena individual de la flota."""

    def __init__(self, ia_juego):
        """Inicializa el alienigena y su posicion de partida."""
        super().__init__()
        self.pantalla = ia_juego.pantalla

        # Cargar imagen y obtener su rect
        self.imagen = pygame.image.load('images/alienigena.bmp')
        self.rect = self.imagen.get_rect()

        # Colocar cerca de la esquina superior izquierda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guardar posicion horizontal como float
        self.x = float(self.rect.x)
```

¿Por que `self.rect.x = self.rect.width`? Para dejar un margen a la izquierda igual al ancho del propio alienigena. Asi no queda pegado al borde.

¿Por que `self.x` como float? Porque mas adelante (P3.11) haremos que la flota se mueva, y necesitaremos velocidades fraccionarias — el mismo patron que usaste en la nave.

---


## Paso 2 -- Mostrar el primer alienigena {#paso-2-mostrar-el-primer-alienigena}

Antes de construir la flota entera, comprueba que un solo alienigena aparece bien en pantalla.


### 2.1 Grupo de alienigenas {#2-dot-1-grupo-de-alienigenas}

En el constructor de `InvasionAlienigena`, crea un grupo y llama a un metodo que construira la flota:

```python
self.alienigenas = pygame.sprite.Group()
self._crear_flota()
```


### 2.2 Metodo `_crear_flota()` (version minima) {#2-dot-2-metodo-crear-flota--version-minima}

Por ahora, crea un solo alienigena para verificar que todo funciona:

```python
def _crear_flota(self):
    """Crea la flota de alienigenas."""
    alienigena = Alienigena(self)
    self.alienigenas.add(alienigena)
```


### 2.3 Dibujar el grupo {#2-dot-3-dibujar-el-grupo}

En `_actualizar_pantalla()` (o en tu fase de dibujo), añade una sola linea:

```python
self.alienigenas.draw(self.pantalla)
```

A diferencia de las balas (que dibujabas una a una con `dibujar_bala()`), los grupos de sprites con imagen se dibujan de golpe con `.draw(superficie)`. Pygame usa el `self.imagen` y `self.rect` de cada sprite del grupo automaticamente.

Ejecuta el juego. Deberia aparecer un alienigena en la esquina superior izquierda.

---


## Paso 3 -- Llenar una fila {#paso-3-llenar-una-fila}

Un solo alienigena no da mucho miedo. Vamos a llenar toda la fila superior.

La idea: coloca alienigenas uno al lado del otro, con un espacio entre ellos igual a su propio ancho. Sigue añadiendo mientras quepan en la pantalla.

```python
def _crear_flota(self):
    """Crea la flota de alienigenas."""
    alienigena = Alienigena(self)
    ancho_alienigena = alienigena.rect.width

    x_actual = ancho_alienigena
    while x_actual < (self.ajustes.ancho_pantalla - 2 * ancho_alienigena):
        self._crear_alienigena(x_actual)
        x_actual += 2 * ancho_alienigena
```

¿Por que `2 * ancho_alienigena`? Porque avanzamos el ancho del alienigena + un espacio igual a su ancho. Asi quedan separados uniformemente.

¿Por que el limite es `ancho_pantalla - 2 * ancho_alienigena`? Para dejar un margen a la derecha y que el ultimo alienigena no quede pegado al borde.


### 3.1 El metodo auxiliar `_crear_alienigena()` {#3-dot-1-el-metodo-auxiliar-crear-alienigena}

Extrae la creacion de cada alienigena a su propio metodo para mantener `_crear_flota()` legible:

```python
def _crear_alienigena(self, x_posicion):
    """Crea un alienigena y lo coloca en la fila."""
    nuevo_alienigena = Alienigena(self)
    nuevo_alienigena.x = x_posicion
    nuevo_alienigena.rect.x = x_posicion
    self.alienigenas.add(nuevo_alienigena)
```

Ejecuta el juego. Deberia aparecer una fila completa de alienigenas arriba.

---


## Paso 4 -- Añadir filas (la flota completa) {#paso-4-añadir-filas--la-flota-completa}

Una fila no es suficiente. Vamos a apilar filas verticalmente hasta llenar la mitad superior de la pantalla.

Envuelve el bucle horizontal en otro bucle vertical:

```python
def _crear_flota(self):
    """Crea la flota completa de alienigenas."""
    alienigena = Alienigena(self)
    ancho_alienigena, alto_alienigena = alienigena.rect.size

    x_actual, y_actual = ancho_alienigena, alto_alienigena
    while y_actual < (self.ajustes.alto_pantalla - 3 * alto_alienigena):
        while x_actual < (self.ajustes.ancho_pantalla - 2 * ancho_alienigena):
            self._crear_alienigena(x_actual, y_actual)
            x_actual += 2 * ancho_alienigena

        # Fila terminada: resetear X, avanzar Y
        x_actual = ancho_alienigena
        y_actual += 2 * alto_alienigena
```

Tres detalles:

-   `alienigena.rect.size` devuelve una tupla `(ancho, alto)` — un atajo para obtener ambas dimensiones
-   El limite vertical es `alto_pantalla - 3 * alto_alienigena` para dejar espacio abajo para la nave y las balas
-   Al terminar cada fila, `x_actual` vuelve al margen izquierdo y `y_actual` baja dos alturas (alienigena + espacio)

Actualiza `_crear_alienigena()` para aceptar la posicion Y:

```python
def _crear_alienigena(self, x_posicion, y_posicion):
    """Crea un alienigena y lo coloca en la flota."""
    nuevo_alienigena = Alienigena(self)
    nuevo_alienigena.x = x_posicion
    nuevo_alienigena.rect.x = x_posicion
    nuevo_alienigena.rect.y = y_posicion
    self.alienigenas.add(nuevo_alienigena)
```

Ejecuta el juego. La pantalla deberia mostrar una flota completa de alienigenas en filas y columnas.

---


## Entrega {#entrega}

-   [ ] `alienigena.py` -- clase `Alienigena(Sprite)` con imagen, rect, posicion float
-   [ ] `invasion_alienigena.py` -- grupo `self.alienigenas`, `_crear_flota()` con filas y columnas, `_crear_alienigena()`, `.draw()` en pantalla
-   [ ] `images/alienigena.bmp` -- imagen del alienigena incluida
-   [ ] La flota aparece correctamente (varias filas, espaciado uniforme)
-   [ ] La nave y las balas siguen funcionando
-   [ ] Pulsar X o Q cierra el juego

&gt;    RECORDATORIO: organiza las entregas por carpetas (P3.6 a P3.10)

---


## BONUS -- Para nota maxima {#bonus-para-nota-maxima}

| **Bonus**                     | **Descripcion**                                                    | **Puntos** |
|-------------------------------|--------------------------------------------------------------------|------------|
| Alienigenas con imagen propia | Usar un sprite personalizado (no el default del libro)             | **+0.5**   |
| Colores alternos por fila     | Filas pares e impares con imagenes o colores diferentes            | **+0.75**  |
| Flota centrada                | Calcular margen para que la flota quede centrada horizontalmente   | **+0.5**   |
| Ajustes en `Ajustes`          | `velocidad_alienigena` preparada (aunque aun no se use)            | **+0.25**  |
| Animacion basica              | Los alienigenas cambian ligeramente de frame (2 sprites alternos)  | **+1**     |
| Contador de alienigenas       | Mostrar en terminal o pantalla cuantos alienigenas hay en la flota | **+0.5**   |

> En la P3.11 la flota cobrara vida: se movera lateralmente, bajara, y podra destruir tu nave. Cuanto mas solida sea tu flota ahora, mas facil sera añadir esa mecanica.

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                              | **Donde lo ves**                                                     |
|-------------------------------------------|----------------------------------------------------------------------|
| **Clase Sprite con imagen**               | `Alienigena(Sprite)` carga `alienigena.bmp` igual que `Nave`         |
| **Group.draw()**                          | Dibuja todos los sprites del grupo de golpe usando su imagen y rect  |
| **Bucles anidados**                       | While externo (filas Y) contiene while interno (columnas X)          |
| **Aritmetica de rects**                   | `rect.size`, `rect.width`, `rect.height` para calcular espaciado     |
| **Refactorizacion: \_crear_alienigena()** | Extraer la creacion individual para que `_crear_flota()` sea legible |
| **Margen calculado**                      | Dejar espacio en bordes: `ancho - 2 * ancho_alien` como limite       |

---


## Rubrica {#rubrica}

| **Criterio**                                                    | **Puntos** |
|-----------------------------------------------------------------|------------|
| `alienigena.py` -- clase completa (Sprite, imagen, rect, float) | 3          |
| `invasion_alienigena.py` -- flota con filas y columnas          | 3          |
| `_crear_alienigena()` -- metodo auxiliar separado               | 1          |
| Imagen `alienigena.bmp` incluida                                | 1          |
| Ejecucion (flota visible, nave+balas funcionan)                 | 2          |
| **Total base**                                                  | **10**     |
| BONUS (hasta +3.5, max 10)                                      | +3.5       |

---

> _"Cuando ves la pantalla llena de enemigos por primera vez, algo cambia. Ya no estas programando — estas creando un mundo."_
