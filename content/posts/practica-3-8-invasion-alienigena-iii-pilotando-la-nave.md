+++
title = "Practica 3.8 - Invasion Alienigena III: Pilotando la Nave"
author = ["Fénix"]
publishDate = 2026-05-01
tags = ["prácticas"]
url = "/pygame3/"
draft = false
+++

{{< figure src="/images/la-nabe.png" >}}


## Objetivo {#objetivo}

Tu nave esta en pantalla, pero es una estatua. En esta practica le vas a dar vida: que responda al teclado y se mueva de lado a lado.

Lo que parece un cambio simple esconde un patron fundamental del desarrollo de videojuegos: el **patron flag + update**. Aprenderlo aqui te servira para todo lo que venga despues (disparos, enemigos, animaciones...).

Al terminar seras capaz de:

-   Gestionar eventos de teclado (`KEYDOWN` y `KEYUP`)
-   Implementar movimiento continuo con banderas booleanas
-   Trabajar con velocidades fraccionarias (float vs int)
-   Limitar el movimiento a los bordes de la pantalla
-   Refactorizar el game loop extrayendo metodos privados

> Basado en el Capitulo 12 de _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Punto de partida {#punto-de-partida}

Tu P3.7 funcional: una ventana con una nave centrada abajo que no se mueve.

```text
PRACTICA3.8/
+-- invasion_alienigena.py   <-- tu P3.7 (lo vas a ampliar)
+-- ajustes.py               <-- tu P3.7 (vas a añadir velocidad_nave)
+-- nave.py                  <-- tu P3.7 (vas a añadir movimiento)
+-- images/
    +-- nave.bmp
```

---


## Paso 1 -- Entender el problema {#paso-1-entender-el-problema}

Cuando pulsas una tecla, Pygame genera un evento `KEYDOWN`. Cuando la sueltas, genera un `KEYUP`. Si simplemente mueves la nave dentro del `KEYDOWN`, ocurre algo frustrante: la nave avanza **un unico paso** por cada pulsacion. Para mantenerla pulsada y que se deslice, necesitas algo mas.

La solucion es separar dos responsabilidades:

-   **Detectar** que el jugador esta pulsando una tecla (en los eventos).
-   **Mover** la nave de verdad (en el bucle de actualizacion, cada frame).

Esto se consigue con banderas (flags).

---


## Paso 2 -- Flags de movimiento en `Nave` {#paso-2-flags-de-movimiento-en-nave}

Añade dos atributos booleanos al constructor de `Nave`:

-   `self.moviendo_derecha = False`
-   `self.moviendo_izquierda = False`

Estos flags no mueven nada por si solos. Son como interruptores: los eventos de teclado los encienden o apagan, y un metodo separado lee su estado para decidir si mover la nave.

---


## Paso 3 -- Responder al teclado {#paso-3-responder-al-teclado}

En `invasion_alienigena.py`, dentro del bloque de eventos del game loop, añade comprobaciones para `KEYDOWN` y `KEYUP`:


### 3.1 Eventos de teclado {#3-dot-1-eventos-de-teclado}

| **Evento**       | **Que ocurre**          |
|------------------|-------------------------|
| `pygame.KEYDOWN` | El jugador pulsa tecla  |
| `pygame.KEYUP`   | El jugador suelta tecla |

Para saber **cual** tecla, comprueba `event.key`:

| **Constante**    | **Tecla**        |
|------------------|------------------|
| `pygame.K_RIGHT` | Flecha derecha   |
| `pygame.K_LEFT`  | Flecha izquierda |
| `pygame.K_q`     | Tecla Q          |


### 3.2 Que hacer en cada evento {#3-dot-2-que-hacer-en-cada-evento}

-   `KEYDOWN` + flecha derecha -&gt; `self.nave.moviendo_derecha = True`
-   `KEYDOWN` + flecha izquierda -&gt; `self.nave.moviendo_izquierda = True`
-   `KEYUP` + flecha derecha -&gt; `self.nave.moviendo_derecha = False`
-   `KEYUP` + flecha izquierda -&gt; `self.nave.moviendo_izquierda = False`

Observa la simetria: `KEYDOWN` enciende, `KEYUP` apaga. Si el jugador mantiene pulsada la flecha derecha, `moviendo_derecha` vale `True` durante todos los frames hasta que la suelta.

---


## Paso 4 -- El metodo `actualizar()` en `Nave` {#paso-4-el-metodo-actualizar-en-nave}

Crea un nuevo metodo en la clase `Nave` que lea los flags y mueva el rectangulo:

```python
def actualizar(self):
    """Mueve la nave si algun flag esta activo."""
    if self.moviendo_derecha:
        self.x += self.ajustes.velocidad_nave
    if self.moviendo_izquierda:
        self.x -= self.ajustes.velocidad_nave

    self.rect.x = self.x
```

Dos detalles importantes:


### ¿Por que `self.x` y no directamente `self.rect.x`? {#por-que-self-dot-x-y-no-directamente-self-dot-rect-dot-x}

Los atributos de un `rect` son enteros. Si tu velocidad es `1.5` pixeles por frame, asignar `self.rect.x +` 1.5= se trunca a `1` cada vez. La solucion: guardar la posicion como float en `self.x` y copiar el resultado al rect al final.

En el constructor añade: `self.x = float(self.rect.x)`


### ¿Por que dos `if` y no `if/elif`? {#por-que-dos-if-y-no-if-elif}

Porque si el jugador pulsa las dos flechas a la vez, queremos que ambas fuerzas se anulen (la nave no se mueve). Con `elif`, solo se procesaria una de las dos.


### 4.1 Velocidad en `Ajustes` {#4-dot-1-velocidad-en-ajustes}

Añade un nuevo atributo en `ajustes.py`:

```python
self.velocidad_nave = 1.5
```

Y en el constructor de `Nave`, guarda la referencia: `self.ajustes = ia_juego.ajustes`


### 4.2 Llamar a `actualizar()` en el game loop {#4-dot-2-llamar-a-actualizar-en-el-game-loop}

En `ejecutar_juego()`, despues de procesar eventos y antes de redibujar, llama a `self.nave.actualizar()`.

El game loop queda asi:

```text
1. Procesar eventos        (KEYDOWN/KEYUP -> activar/desactivar flags)
2. Actualizar estado       (nave.actualizar() -> mover si flag activo)
3. Redibujar pantalla      (fill -> nave.dibujarme -> flip)
```

---


## Paso 5 -- Limitar a los bordes {#paso-5-limitar-a-los-bordes}

Sin limites, la nave desaparece por los lados. Añade comprobaciones en `actualizar()`:

-   Solo mover a la derecha si `self.rect.right < self.rect_pantalla.right`
-   Solo mover a la izquierda si `self.rect.left > 0`

Estas condiciones van **dentro** de los `if` de movimiento, antes de modificar `self.x`.

---


## Paso 6 -- Refactorizar: `_verificar_eventos()` {#paso-6-refactorizar-verificar-eventos}

El game loop se ha complicado. Extrae toda la gestion de eventos (`QUIT`, `KEYDOWN`, `KEYUP`) a un metodo privado llamado `_verificar_eventos()`.

> El guion bajo `_` al inicio es una convencion de Python que indica "este metodo es interno, no lo llames desde fuera de la clase".

En `ejecutar_juego()`, reemplaza el bloque `for event in ...` por una sola llamada: `self._verificar_eventos()`.

El game loop queda limpio y legible:

```python
def ejecutar_juego(self):
    while True:
        self._verificar_eventos()
        self.nave.actualizar()

        self.pantalla.fill(self.ajustes.color_fondo)
        self.nave.dibujarme()
        pygame.display.flip()
        self.clock.tick(60)
```

Cinco lineas. Cada una hace una cosa. Eso es buen codigo.

---


## Entrega {#entrega}

-   [ ] `ajustes.py` -- con `velocidad_nave` añadido
-   [ ] `nave.py` -- flags, `actualizar()` con limites, `dibujarme()`
-   [ ] `invasion_alienigena.py` -- `_verificar_eventos()`, llama a `actualizar()`
-   [ ] La nave se mueve con las flechas sin salir de pantalla
-   [ ] Pulsar la X cierra el juego limpiamente

&gt;    RECORDATORIO: organiza las entregas por carpetas (P3.6-Pygame1, P3.7-Pygame2, P3.8-Pygame3...)

---


## BONUS -- Para nota maxima {#bonus-para-nota-maxima}

| **Bonus**                      | **Descripcion**                                              | **Puntos** |
|--------------------------------|--------------------------------------------------------------|------------|
| Salir con Q                    | `pygame.K_q` cierra el juego                                 | **+0.25**  |
| Centrar nave con C             | `pygame.K_c` devuelve la nave al centro (metodo dedicado)    | **+0.5**   |
| `_verificar_pulsacion_tecla()` | Extraer la logica de KEYDOWN a su propio metodo              | **+0.5**   |
| `_verificar_soltado_tecla()`   | Extraer la logica de KEYUP a su propio metodo                | **+0.5**   |
| Velocidad variable             | Shift + flecha = velocidad doble (o teclas +/- para ajustar) | **+0.75**  |
| Movimiento vertical            | Flechas arriba/abajo mueven la nave (con limites)            | **+0.5**   |

> Los bonus de refactorizacion allanan el camino para la P3.9 (en la que añadiremos a la nave la capacidad de disparar). Cuanto mas limpio sea tu codigo fuente ahora, mas facil sera añadir mecanicas nuevas.

---

{{< figure src="/images/movimiento-fluido-en-pygame.png" >}}


## Conceptos clave {#conceptos-clave}

| **Concepto**                   | **Donde lo ves**                                                |
|--------------------------------|-----------------------------------------------------------------|
| **KEYDOWN / KEYUP**            | Detectar pulsacion y soltado de teclas                          |
| **Patron flag + update**       | Flag activado en evento, movimiento real en `actualizar()`      |
| **Posicion float vs rect int** | `self.x` guarda decimales, `self.rect.x` recibe entero truncado |
| **Limites de pantalla**        | `rect.right` y `rect.left` frente a los bordes                  |
| **Metodos privados (_)**       | `_verificar_eventos()` -- convencion de uso interno             |
| **Game loop completo**         | eventos -&gt; actualizar -&gt; redibujar (3 fases claras)       |
| **Velocidad configurable**     | `velocidad_nave` centralizada en `Ajustes`                      |

---


## Rubrica {#rubrica}

| **Criterio**                                       | **Puntos** |
|----------------------------------------------------|------------|
| `nave.py` -- flags + `actualizar()` con limites    | 4          |
| `invasion_alienigena.py` -- `_verificar_eventos()` | 3          |
| `ajustes.py` -- `velocidad_nave` añadido           | 1          |
| Ejecucion (nave se mueve sin salir de pantalla)    | 2          |
| **Total base**                                     | **10**     |
| BONUS (hasta +3, max 10)                           | +3         |

---

> _"En los videojuegos, el input del jugador es sagrado. Si la nave no responde al instante, el juego esta roto."_ -- Cualquier game designer
