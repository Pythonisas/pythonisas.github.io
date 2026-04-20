+++
title = "Práctica 3.6 — Invasión Alienígena I: El esqueleto del juego"
author = ["Jordi"]
date = 2026-04-20T12:00:00+02:00
publishDate = 2026-04-20
tags = ["prácticas"]
url = "/pygame1/"
draft = false
+++

{{< figure src="/images/space-invaders_retro3.jpg" >}}


## Descripcion {#descripcion}

Vamos a construir el esqueleto de un juego llamado **Invasión Alienígena** usando [Pygame](https://www.pygame.org/). Al finalizar esta practica seras capaz de crear una ventana grafica, separar la configuracion en su propio modulo, implementar el _game loop_ y gestionar eventos.

> 📖 Basado en el Capítulo 12 de _Python Crash Course, 3rd Edition_ — Eric Matthes

---


## Preparacion del entorno {#preparacion-del-entorno}


### Instalar Pygame {#instalar-pygame}

```bash
python3 -m pip install --user pygame
```

Verifica:

```bash
python3 -c "import pygame; print(pygame.ver)"
```


### Estructura del proyecto {#estructura-del-proyecto}

```text
PRACTICA3.6/
├── alien_invasion.py   ← Programa principal (completa los huecos)
└── settings.py         ← Configuración del juego (se da completo)
```

---


## Paso 1 — La clase `Settings` {#paso-1-la-clase-settings}

Antes de escribir el juego, creamos un modulo aparte con _todos_ los valores configurables. Asi evitamos numeros magicos dispersos por el codigo.

¿Por que una clase y no simples constantes?

1.  **Un solo lugar** donde cambiar valores
2.  **Un solo objeto** que pasamos a las demas partes del juego
3.  Mas adelante podremos añadir _ajustes dinamicos_ sin tocar el resto


### `settings.py` — Se te da completo {#settings-dot-py-se-te-da-completo}

```python
class Settings:
    """Clase que almacena toda la configuración de Invasión Alienígena."""

    def __init__(self):
        """Inicializa los ajustes del juego."""
        # Ajustes de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
```

| **Linea**        | **¿Que hace?**                                                    |
|------------------|-------------------------------------------------------------------|
| `class Settings` | Define la clase. No hereda de nada (objeto simple).               |
| `__init__`       | Constructor: se ejecuta al crear `Settings()`.                    |
| `screen_width`   | Ancho de la ventana en pixeles.                                   |
| `screen_height`  | Alto de la ventana en pixeles.                                    |
| `bg_color`       | Color de fondo como tupla RGB `(R, G, B)`. Aqui es un gris claro. |

---


## Paso 2 — Completa `alien_invasion.py` {#paso-2-completa-alien-invasion-dot-py}

Tu trabajo: **completa los huecos marcados con `___`**.


### 2.1 — Las importaciones {#2-dot-1-las-importaciones}

```python
import ___

import ___

from ___ import ___
```

| **Modulo** | **¿Para que?**                                                 |
|------------|----------------------------------------------------------------|
| `sys`      | Para `sys.exit()`: salir limpiamente del programa.             |
| `pygame`   | La biblioteca grafica que gestiona ventana, eventos, dibujo... |
| `Settings` | Nuestra clase de configuracion (del archivo `settings.py`).    |

> 💡 Convencion PEP 8: primero _biblioteca estandar_ (`sys`), despues _terceros_
> (`pygame`), y por ultimo _propios_ (`Settings`).


### 2.2 — La clase `AlienInvasion` y su constructor {#2-dot-2-la-clase-alieninvasion-y-su-constructor}

```python
class AlienInvasion:
    """Clase principal que gestiona los recursos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa el juego y crea los recursos."""
        ___.init()
        self.clock = ___.time.Clock()
        self.settings = ___()

        self.screen = ___.display.set_mode(
            (self.settings.___, self.settings.___))
        ___.display.set_caption("Alien Invasion")
```

| **Instruccion**                | **¿Que hace?**                                                                       |
|--------------------------------|--------------------------------------------------------------------------------------|
| `pygame.init()`                | Inicializa todos los subsistemas de Pygame (video, audio, eventos...).               |
| `pygame.time.Clock()`          | Crea un reloj para controlar los FPS (fotogramas por segundo).                       |
| `Settings()`                   | Crea una instancia de nuestra configuracion y la guarda en `self.settings`.          |
| `pygame.display.set_mode(...)` | Crea la ventana del juego con las dimensiones de `settings`. Devuelve una _surface_. |
| `set_caption(...)`             | Pone el titulo de la ventana.                                                        |

> 💡 **¿Que es una _surface_?** En Pygame, una _surface_ es un lienzo rectangular
> donde se pueden dibujar imagenes, formas y texto. La pantalla completa
> (`self.screen`) es la _surface_ principal.


### 2.3 — El bucle principal: `run_game()` {#2-dot-3-el-bucle-principal-run-game}

El corazon de todo videojuego es un bucle infinito que repite tres pasos:

1.  **Leer eventos** (teclado, raton, cierre de ventana)
2.  **Actualizar estado** (mover objetos, comprobar colisiones)
3.  **Redibujar pantalla** (pintar todo de nuevo)

<!--listend-->

```python
def run_game(self):
    """Inicia el bucle principal del juego."""
    while ___:
        # 1. Vigilar eventos de teclado y raton.
        for event in ___.event.get():
            if event.type == ___.___ :
                sys.___()

        # 2. (Por ahora no hay nada que actualizar)

        # 3. Redibujar la pantalla en cada pasada del bucle.
        self.screen.___(self.settings.___)

        # Hacer visible la pantalla recien dibujada.
        ___.display.___()
        self.clock.___(60)
```

| **Instruccion**         | **¿Que hace?**                                                                 |
|-------------------------|--------------------------------------------------------------------------------|
| `while True`            | Bucle infinito: el juego corre hasta que el jugador cierre la ventana.         |
| `pygame.event.get()`    | Devuelve la lista de eventos pendientes (teclas, clics, cierre...).            |
| `pygame.QUIT`           | Evento que se dispara al pulsar la ✕ de la ventana.                            |
| `sys.exit()`            | Termina el programa limpiamente.                                               |
| `self.screen.fill(...)` | Pinta toda la pantalla con el color de fondo (borra el fotograma anterior).    |
| `pygame.display.flip()` | Intercambia el bufer: muestra lo que acabamos de dibujar.                      |
| `self.clock.tick(60)`   | Limita el bucle a 60 FPS. Sin esto, el bucle correria tan rapido como pudiese. |

> 💡 **¿Por que `flip()` y no dibujar directamente?**
> Pygame usa _doble bufer_: dibujamos en un bufer oculto y luego lo
> intercambiamos con el visible. Esto evita parpadeos (_flickering_).


### 2.4 — El punto de entrada {#2-dot-4-el-punto-de-entrada}

```python
if __name__ == '___':
    # Crear una instancia del juego y ejecutarlo.
    ai = ___()
    ai.___()
```

---


## Entrega {#entrega}

-   [ ] `settings.py` — completo y funcional
-   [ ] `alien_invasion.py` — con todos los huecos completados
-   [ ] Al ejecutar `python3 alien_invasion.py` se abre una ventana que se cierra con la ✕

---


## BONUS — Para nota maxima {#bonus-para-nota-maxima}

| **Bonus**               | **Descripcion**                                   | **Puntos** |
|-------------------------|---------------------------------------------------|------------|
| 🌑 Fondo espacial       | Color de fondo azul oscuro tipo espacio           | **+0.25**  |
| 🖥️ Pantalla completa     | `pygame.FULLSCREEN` + detectar resolucion         | **+0.75**  |
| 🚀 Sprite de nave       | Imagen de nave centrada en parte inferior         | **+1**     |
| ⬅️➡️ Movimiento de nave   | Flechas izquierda/derecha con `KEYDOWN` y `KEYUP` | **+1**     |

> 💡 Los dos ultimos bonus anticipan la Practica 3.7. Si los implementas aqui, llevaras ventaja.

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                | **Donde lo ves**                                                    |
|-----------------------------|---------------------------------------------------------------------|
| **Composicion**             | `AlienInvasion` tiene `self.settings = Settings()`                  |
| **Game loop**               | `while True` + eventos + redibujado + FPS                           |
| **Surface y doble bufer**   | `self.screen` es la surface principal, `flip()` intercambia buferes |
| **Eventos Pygame**          | `pygame.event.get()` + `pygame.QUIT`                                |
| **Modulo de configuracion** | `settings.py` — un solo lugar para todos los ajustes                |

---


## Rubrica {#rubrica}

| **Criterio**                             | **Puntos** |
|------------------------------------------|------------|
| `settings.py` correcto                   | 1          |
| Imports correctos (PEP 8)                | 1          |
| Constructor `AlienInvasion` completo     | 2.5        |
| Game loop (eventos + fill + flip + tick) | 3          |
| Punto de entrada `__main__`              | 0.5        |
| Ejecucion sin errores                    | 1          |
| Codigo limpio                            | 1          |
| **Total base**                           | **10**     |
| BONUS (hasta +3, max 10)                 | +3         |

---

> _"Todo gran juego empezo siendo una ventana vacia."_ 🎮
