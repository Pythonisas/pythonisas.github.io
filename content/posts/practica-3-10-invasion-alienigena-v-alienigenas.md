+++
title = "Practica 3.10 - Invasion Alienigena V: Alienigenas!"
author = ["Jordi"]
tags = ["prácticas"]
url = "/pygame5/"
draft = false
+++

## Mision: Llenar el cielo de enemigos {#mision-llenar-el-cielo-de-enemigos}

**Contexto galactico:** Tus armas funcionan, pero los radares muestran una señal inquietante: los alienigenas se acercan en formacion. Los estrategas de la Resistencia necesitan que llenes la mitad superior de la pantalla con una flota enemiga — organizados en filas y columnas, como un ejercito que avanza.

El reto no es solo "poner sprites": es un problema de **generacion procedural**. ¿Cuantos alienigenas caben en una fila? ¿Cuantas filas caben antes de llegar a la zona de la nave? Tu codigo debe calcularlo automaticamente segun el tamaño de la pantalla y del sprite — sin numeros magicos hardcodeados.

> Basado en el Capitulo 13 de _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Los problemas de ingenieria {#los-problemas-de-ingenieria}

1.  **El sprite individual** — Necesitas una clase `Alienigena` que cargue una imagen y se posicione con margenes correctos. Similar a `Nave`, pero con un detalle: `self.x` como float (¿para que, si todavia no se mueve? Piensalo — o lo descubriras en P3.11)

2.  **La generacion procedural** — ¿Cuantos alienigenas caben en una fila? No puedes hardcodear "8 alienigenas". Si cambias el tamaño de la pantalla o del sprite, el numero debe recalcularse solo. Necesitas aritmetica de rects

3.  **La dimension vertical** — Una fila no es suficiente. Necesitas apilar filas, dejando espacio entre ellas y reservando la zona inferior para la nave. Esto requiere bucles anidados

4.  **Dibujar 50 sprites de golpe** — Con las balas, las dibujabas una a una. Con 50 alienigenas, eso es ineficiente. Pygame ofrece `Group.draw()` — una sola llamada que dibuja todo el grupo

---


## Herramientas a tu disposicion {#herramientas-a-tu-disposicion}

| **Herramienta**          | **Para que sirve**                                                      |
|--------------------------|-------------------------------------------------------------------------|
| `pygame.sprite.Sprite`   | Tu `Alienigena` hereda de aqui (igual que `Bala`)                       |
| `pygame.image.load()`    | Cargar la imagen del alien desde `images/alienigena.bmp`                |
| `.get_rect()`            | Obtener el rectangulo de la imagen (con `.width`, `.height`, `.size`)   |
| `Group.draw(superficie)` | Dibuja todos los sprites del grupo de golpe usando su `imagen` y `rect` |
| `rect.size`              | Devuelve `(ancho, alto)` — atajo para ambas dimensiones                 |

Necesitaras una imagen para el alienigena. Puedes usar la del libro ([recursos PCC](https://ehmatthes.github.io/pcc_3e)) o buscar una propia. Guardala en `images/alienigena.bmp`.

---


## Desafio 1: El primer alien {#desafio-1-el-primer-alien}

Antes de construir la flota, haz que aparezca **un solo alienigena** en la esquina superior izquierda. Si uno funciona, 50 funcionaran.

**Requisitos:**

-   Nuevo fichero `alienigena.py` con clase `Alienigena(Sprite)`
-   Carga `images/alienigena.bmp` y obtiene su `rect`
-   Se posiciona con un margen: `self.rect.x = self.rect.width` (un ancho de distancia al borde)
-   Se guarda `self.x = float(self.rect.x)` (¿por que float si no se mueve? Pregunta de diseño para P3.11)
-   Crea un `pygame.sprite.Group` en `InvasionAlienigena` y usa `.draw()` para pintarlo

**Diagnostico:** ejecuta el juego. Deberia aparecer un alien arriba a la izquierda. Si no lo ves, revisa que llamas a `.draw()` en la fase de dibujo.

---


## Desafio 2: La primera fila {#desafio-2-la-primera-fila}

Un solo alien no da miedo. Llena toda la fila superior.

**El problema:** ¿cuantos alienigenas caben? Depende del ancho de la pantalla y del ancho del sprite. Tu codigo debe calcularlo, no hardcodearlo.

**Pistas de diseño:**

-   El espaciado entre aliens es igual al ancho de un alien (asi quedan uniformes)
-   El margen derecho: deja al menos 2 anchos de alien libres para que no quede pegado al borde
-   Usa un `while` que incremente la posicion X en `2 * ancho_alienigena` en cada iteracion
-   Extrae la creacion individual a `_crear_alienigena(x_posicion)` para mantener `_crear_flota()` legible

**Diagnostico:** `print(len(self.alienigenas))` te dice cuantos aliens has generado. ¿Cambia si modificas `ancho_pantalla` en `Ajustes`? Si no cambia, algo esta hardcodeado.

---


## Desafio 3: La flota completa {#desafio-3-la-flota-completa}

Una fila es el principio. Ahora apila filas verticalmente hasta llenar la mitad superior de la pantalla.

**El problema:** ¿cuantas filas caben? Necesitas reservar espacio abajo para la nave y las balas (al menos 3 alturas de alien).

**Pista:** envuelve tu bucle horizontal en otro bucle vertical. El externo controla Y (filas), el interno controla X (columnas). Al terminar cada fila, resetea X al margen izquierdo y avanza Y.

**Diagnostico:** el `print(len(self.alienigenas))` deberia mostrar decenas de aliens. Si cambias `alto_pantalla`, deberian aparecer mas o menos filas automaticamente.

---


## Entrega {#entrega}

```text
PRACTICA3.10/
+-- invasion_alienigena.py
+-- ajustes.py
+-- nave.py
+-- bala.py
+-- alienigena.py            <-- NUEVO
+-- images/
    +-- nave.bmp
    +-- alienigena.bmp       <-- NUEVA
```

Requisitos funcionales:

-   [ ] La flota aparece con varias filas y columnas, espaciado uniforme
-   [ ] El numero de aliens se calcula automaticamente (sin numeros magicos)
-   [ ] `_crear_alienigena()` como metodo auxiliar separado
-   [ ] La nave y las balas siguen funcionando
-   [ ] `Group.draw()` para pintar toda la flota de golpe

---


## Rubrica por competencias {#rubrica-por-competencias}

| **Criterio**                               | **Maestro (9-10)**                                                   | **Aprendiz (6-8)**                                 | **Recluta (0-5)**                   | **Peso** |
|--------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------|-------------------------------------|----------|
| **Clase Alienigena**                       | Hereda de Sprite, imagen cargada, rect con margenes, float preparado | Funciona pero margenes hardcodeados o sin float    | No hay clase o no carga imagen      | **25%**  |
| **Generacion procedural (filas+columnas)** | Bucles anidados que calculan posiciones segun tamaño pantalla/sprite | Una fila funciona pero filas multiples incompletas | Aliens posicionados manualmente     | **30%**  |
| **Arquitectura (_crear_alienigena)**       | Metodo auxiliar extraido, `_crear_flota()` legible                   | Funciona pero toda la logica en un solo metodo     | Sin separacion de responsabilidades | **20%**  |
| **Group.draw() y ejecucion**               | Flota visible, nave+balas funcionan, `.draw()` usado                 | Flota aparece pero con errores visuales menores    | No ejecuta o flota no visible       | **15%**  |
| **Pensamiento critico / IA**               | Explica por que float, documenta prompts                             | Indica uso de IA sin explicar decisiones           | Copia sin comprension               | **10%**  |

---


## Bonus de ingenieria (hasta +2.5) {#bonus-de-ingenieria--hasta-plus-2-dot-5}

| **Bonus**                 | **Descripcion**                                      | **Puntos** |
|---------------------------|------------------------------------------------------|------------|
| Sprite personalizado      | Imagen propia en vez del default del libro           | **+0.5**   |
| Flota centrada            | Calculo de margen para centrado horizontal           | **+0.5**   |
| Colores alternos por fila | Filas pares e impares con sprites o tonos diferentes | **+0.75**  |
| Animacion basica          | 2 frames alternos para los alienigenas               | **+1.0**   |

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                | **Donde lo ves**                                                    |
|-----------------------------|---------------------------------------------------------------------|
| **Sprite con imagen**       | `Alienigena(Sprite)` carga `alienigena.bmp` igual que `Nave`        |
| **Group.draw()**            | Una llamada dibuja todos los sprites del grupo                      |
| **Generacion procedural**   | Bucles que calculan cuantos aliens caben segun dimensiones          |
| **Bucles anidados**         | While externo (filas Y) contiene while interno (columnas X)         |
| **Aritmetica de rects**     | `rect.size`, `rect.width`, `rect.height` para calcular espaciado    |
| **Margenes calculados**     | `ancho_pantalla - 2 * ancho_alien` como limite — no numeros magicos |
| **Preparar para el futuro** | `self.x = float(...)` aunque el alien aun no se mueva               |

---

> _"Cuando ves la pantalla llena de enemigos por primera vez, algo cambia. Ya no estas programando — estas creando un mundo."_
