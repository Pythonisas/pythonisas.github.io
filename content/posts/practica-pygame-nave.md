+++
title = "Practica 3.7 - Invasion Alienigena II: Añadiendo-la-imagen-de-la-Nave"
author = ["Fénix"]
date = 2026-04-27T12:00:00+02:00
publishDate = 2026-04-27
tags = ["practicas"]
url = "/pygame2/"
draft = false
+++

{{< figure src="/images/nave.png" >}}


## Objetivo {#objetivo}

Ya tienes un juego que abre una ventana, pinta un fondo y cierra limpiamente. Lo que falta es lo mas importante: **algo que mirar**.

En esta practica vas a colocar una nave espacial en la parte inferior de la pantalla. Parece poco, pero por el camino aprenderas tres ideas que usaras en todo lo que viene despues:

1.  **Cargar una imagen** desde disco y convertirla en algo que Pygame sabe dibujar (una _surface_).
2.  **Posicionar un elemento** usando rectangulos (`rect`), el sistema de coordenadas que Pygame usa para todo.
3.  **Ampliar la arquitectura** del juego con una segunda clase (`Nave`) que se compone dentro de `InvasionAlienigena`, igual que `Ajustes`.

> Basado en el Capitulo 12 de _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Punto de partida {#punto-de-partida}

```text
PRACTICA3.7/
+-- invasion_alienigena.py   <-- tu P3.6 (lo vas a ampliar)
+-- ajustes.py               <-- tu P3.6 (sin cambios)
+-- nave.py                  <-- NUEVO: la clase Nave
+-- images/
    +-- nave.bmp             <-- NUEVO: tu sprite
```

> **Busca tu propia imagen de nave.** Formato `.bmp`, `.png` o `.jpg`. Intenta que el fondo sea transparente o del mismo color que tu `color_fondo`. Puedes inspirarte en [OpenGameArt](https://opengameart.org), [itch.io](https://itch.io/game-assets/free/tag-sprites) o [Piskel](https://www.piskelapp.com/) (para dibujarla tu mismo).

---


## Paso 1 -- La clase `Nave` (`nave.py`) {#paso-1-la-clase-nave--nave-dot-py}

Crea un fichero `nave.py` con una clase que sepa **donde esta** la nave y **como dibujarse**. Nada mas, por ahora.


### 1.1 El constructor {#1-dot-1-el-constructor}

El constructor recibe la instancia del juego (`ia_juego`) para acceder a la pantalla. Con esa referencia necesitas:

| **Que hacer**              | **Como**                                             |
|----------------------------|------------------------------------------------------|
| Guardar la pantalla        | `self.pantalla = ia_juego.pantalla`                  |
| Dimensiones de la pantalla | `self.rect_pantalla = ia_juego.pantalla.get_rect()`  |
| Cargar la imagen           | `self.imagen = pygame.image.load('images/nave.bmp')` |
| Rectangulo de la imagen    | `self.rect = self.imagen.get_rect()`                 |
| Posicionar centro-abajo    | `self.rect.midbottom = self.rect_pantalla.midbottom` |

> **¿Que es un `rect`?** Pygame representa la posicion y el tamanyo de cualquier elemento como un rectangulo. Un `rect` tiene atributos como `center`, `midbottom`, `left`, `right`, `x`, `y`. Asigna un valor y Pygame recoloca el rectangulo. El origen `(0, 0)` esta en la esquina **superior izquierda** de la ventana.


### 1.2 El metodo `dibujarme()` {#1-dot-2-el-metodo-dibujarme}

Una sola linea: pinta la imagen en la pantalla, en la posicion de `self.rect`. La funcion que necesitas es `blit()` (_Block Image Transfer_). Se llama sobre la surface destino (la pantalla) y recibe la surface origen (la imagen) y la posicion (el rect).

---


## Paso 2 -- Conectar `Nave` con el juego {#paso-2-conectar-nave-con-el-juego}

Tres cambios en `invasion_alienigena.py`:

1.  **Importar** `Nave` (igual que ya importas `Ajustes`).
2.  **Crear la instancia**: `self.nave = Nave(self)` en el constructor, **despues** de crear la pantalla.
3.  **Dibujar** en cada vuelta del game loop. El orden es critico:

<!--listend-->

```text
fill()           <-- 1. pintar fondo (borra el frame anterior)
nave.dibujarme() <-- 2. pintar nave encima del fondo
flip()           <-- 3. mostrar el frame completo
```

Si dibujas la nave antes de `fill()`, el fondo la tapa. Si la dibujas despues de `flip()`, se queda en el bufer oculto.

**Prueba:** ejecuta tu juego. La nave deberia aparecer centrada abajo. Si no la ves: ¿la ruta de la imagen es correcta? ¿llamas a `dibujarme()` entre `fill()` y `flip()`?

---


## Entrega {#entrega}

-   [ ] `ajustes.py` -- sin cambios respecto a P3.6 (pero incluyelo)
-   [ ] `nave.py` -- clase `Nave` con constructor y `dibujarme()`
-   [ ] `invasion_alienigena.py` -- importa `Nave`, crea instancia, la dibuja
-   [ ] `images/nave.bmp` (o `.png`) -- tu imagen de nave
-   [ ] Al ejecutar: ventana con la nave visible centrada en la parte inferior

&gt;    RECORDATORIO: organiza las entregas por carpetas (P3.6-Pygame1, P3.7-Pygame2...)

---


## BONUS -- Para nota maxima {#bonus-para-nota-maxima}

| **Bonus**                 | **Descripcion**                                               | **Puntos** |
|---------------------------|---------------------------------------------------------------|------------|
| Fondo espacial            | Cambia `color_fondo` a un tono oscuro tipo espacio            | **+0.5**   |
| Segundo sprite decorativo | Otro elemento grafico (estrella, planeta) con su propia clase | **+1**     |
| Movimiento con flechas    | La nave se mueve izquierda/derecha con las teclas de flecha   | **+1.5**   |

> El ultimo bonus anticipa la Practica 3.8. Si lo implementas aqui, llevaras ventaja.

---


## Conceptos clave : {#conceptos-clave}

{{< figure src="/images/Guia-de-inicio_Arquitectura-de-un-Juego-en-Pygame.png" >}}

---


## Rubrica {#rubrica}

| **Criterio**                                 | **Puntos** |
|----------------------------------------------|------------|
| `nave.py` -- clase Nave completa             | 5          |
| `invasion_alienigena.py` -- integracion Nave | 3          |
| `ajustes.py` + imagen incluida               | 1          |
| Ejecucion (nave visible centrada abajo)      | 1          |
| **Total base**                               | **10**     |
| BONUS (hasta +3, max 10)                     | +3         |

---

> _"Un pixel bien colocado vale mas que mil lineas de codigo."_
