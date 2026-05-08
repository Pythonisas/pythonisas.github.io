+++
title = "Practica 3.9 - Invasion Alienigena IV: Disparando Balas"
author = ["Fénix"]
publishDate = 2026-05-01
tags = ["prácticas"]
url = "/pygame4/"
draft = false
+++

{{< figure src="/images/space-invaders.png" >}}


## Mision: El Condensador de Particulas {#mision-el-condensador-de-particulas}

**Contexto galactico:** La nave ya se desplaza por el cuadrante, pero la inteligencia de la Resistencia informa que los alienigenas estan a punto de entrar en rango. Los ingenieros han instalado un cañon de plasma experimental, pero el software de control es inestable.

Tu mision no es solo "hacer que dispare", sino resolver tres problemas criticos de ingenieria que podrian destruir el computador de a bordo en plena batalla.

> Basado en el Capitulo 12 de _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Los problemas de ingenieria {#los-problemas-de-ingenieria}

Como desarrollador/a jefe del proyecto, te enfrentas a:

1.  **Las balas fantasma (Fuga de memoria)** — En las pruebas iniciales, cada bala disparada sigue existiendo en el sistema incluso despues de salir de pantalla. Si el piloto dispara demasiado, el juego se ralentiza hasta colapsar. ¿Como detectas y eliminas estos objetos fantasma?

2.  **Gestion de energia (Recurso limitado)** — El condensador de la nave no es infinito. Si el jugador puede disparar sin limite, el juego pierde toda tension. Este valor debe ser ajustable sin tocar el codigo de la bala.

3.  **Arquitectura modular** — No queremos codigo monolitico. El flujo de eventos, la actualizacion de posiciones y la limpieza de memoria deben vivir en metodos independientes y limpios.

---


## Herramientas a tu disposicion {#herramientas-a-tu-disposicion}

Antes de empezar, familiarizate con estas piezas de Pygame:

| **Herramienta**                      | **Para que sirve**                                                                           |
|--------------------------------------|----------------------------------------------------------------------------------------------|
| `pygame.sprite.Sprite`               | Clase base para objetos agrupables. Tu `Bala` heredara de ella                               |
| `pygame.sprite.Group`                | Coleccion con superpoderes: `.update()` actualiza todos, `.add()` / `.remove()` los gestiona |
| `pygame.Rect(x, y, ancho, alto)`     | Crea un rectangulo sin imagen (la bala no necesita un .bmp)                                  |
| `pygame.draw.rect(sup, color, rect)` | Dibuja un rectangulo solido en pantalla                                                      |

---


## Desafio 1: Armar la nave {#desafio-1-armar-la-nave}

Tu nave necesita poder disparar. Cuando el jugador pulse `ESPACIO`:

-   Se crea una bala nueva en la punta de la nave
-   La bala sube a velocidad constante
-   Se dibuja como un rectangulo solido (sin imagen)

**Requisitos tecnicos:**

-   Nuevo fichero `bala.py` con clase que hereda de `Sprite`
-   Metodos: `actualizar()` (mover hacia arriba) y `dibujar_bala()` (pintar el rectangulo)
-   El `rect` de la bala se construye con `pygame.Rect()` y se posiciona en `ia_juego.nave.rect.midtop`
-   Patron float para velocidades fraccionarias: `self.y = float(self.rect.y)`
-   Centraliza los ajustes (velocidad, tamaño, color) en `ajustes.py`
-   Usa un `pygame.sprite.Group` para almacenar todas las balas activas

---


## Desafio 2: Diagnosticar la fuga de memoria {#desafio-2-diagnosticar-la-fuga-de-memoria}

Implementa el disparo y ejecuta el juego. Ahora añade esta linea de diagnostico en tu game loop, despues de actualizar las balas:

```python
print(len(self.balas))
```

Dispara 10 veces y observa la consola:

-   ¿El numero baja cuando las balas salen de pantalla?
-   ¿O sigue subiendo indefinidamente?

Si no baja, tienes una **fuga de memoria**: las balas siguen vivas consumiendo recursos aunque no se vean.

**Tu mision:** programa una rutina que elimine fisicamente las balas del grupo cuando `bala.rect.bottom <` 0=.

**Trampa tecnica:** Python no permite modificar una coleccion mientras la recorres. ¿Como iteras sobre las balas para borrar las que sobran sin romper el bucle?

**IMPORTANTE:** una vez verificado, **elimina el `print()`**. Escribir en consola cada frame ralentiza mas que dibujar graficos.

---


## Desafio 3: Energia limitada {#desafio-3-energia-limitada}

Sin limite, el jugador puede inundar la pantalla manteniendo ESPACIO pulsado. Eso destruye el diseño del juego.

**Tu mision:** limita a 3 balas simultaneas. Si ya hay 3, pulsar ESPACIO no hace nada hasta que alguna desaparezca.

**Pregunta de diseño (incluye la respuesta en un comentario de tu codigo):** ¿Donde colocas este limite? ¿En la clase `Bala`, en el metodo de disparo, o en `Ajustes`? ¿Por que?

---


## Desafio 4: Arquitectura limpia {#desafio-4-arquitectura-limpia}

Tu game loop se ha complicado. Tienes logica de eventos, actualizacion de nave, actualizacion de balas, limpieza de balas y dibujo — todo entremezclado.

**Tu mision:** extrae la logica de balas a un metodo privado `_actualizar_balas()`. El game loop deberia quedar en 5-6 lineas legibles, donde cada linea describe **que** se hace, no **como**.

---


## Entrega {#entrega}

```text
PRACTICA3.9/
+-- invasion_alienigena.py
+-- ajustes.py
+-- nave.py
+-- bala.py                  <-- NUEVO
+-- images/
    +-- nave.bmp
```

Requisitos funcionales:

-   [ ] ESPACIO dispara balas que suben desde la nave
-   [ ] Las balas desaparecen al salir de pantalla (sin fuga de memoria)
-   [ ] Maximo 3 balas simultaneas
-   [ ] El game loop esta limpio (metodos privados)
-   [ ] El juego no se ralentiza despues de 100 disparos

---


## Uso etico y critico de la IA {#uso-etico-y-critico-de-la-ia}

En esta practica, el uso de herramientas de IA (ChatGPT, Claude, Copilot) esta **permitido** bajo estas condiciones:

1.  **Transparencia:** si usas un prompt para generar codigo, incluyelo como comentario multilínea al inicio del fichero
2.  **Comprension:** debes ser capaz de explicar por que iteramos sobre una **copia** del grupo (`self.balas.copy()`) para eliminar elementos

Quien copia sin entender obtiene codigo que funciona hoy y se rompe mañana. Quien entiende lo que copia, lo puede adaptar a cualquier problema futuro.

---


## Rubrica por competencias {#rubrica-por-competencias}

| **Criterio**                       | **Maestro (9-10)**                                                                     | **Aprendiz (6-8)**                                              | **Recluta (0-5)**                    | **Peso** |
|------------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------|--------------------------------------|----------|
| **Ingenieria de la clase Bala**    | Hereda de Sprite, `super()`, rect dinamico en la punta de la nave, float para posicion | Funciona pero posicionamiento rigido o sin herencia optima      | No hay clase Bala o no usa rects     | **30%**  |
| **Gestion de memoria y recursos**  | Diagnostica con `print()`, elimina con `.copy()`, explica por que es necesario         | Elimina balas pero sin demostrar comprension del problema       | Balas se acumulan infinitamente      | **30%**  |
| **Arquitectura y refactorizacion** | Game loop limpio. `_actualizar_balas()` y `_disparar_bala()` extraidos                 | Funciona pero metodos sobrecargados (mezcla eventos con dibujo) | Todo dentro de `ejecutar_juego()`    | **20%**  |
| **Configuracion centralizada**     | Todos los parametros en `Ajustes`. Limite funcional                                    | Algunos valores hardcodeados en vez de en Ajustes               | Sin control de limites o sin ajustes | **10%**  |
| **Pensamiento critico / IA**       | Documenta prompts, justifica decisiones tecnicas                                       | Indica uso de IA pero sin explicar la logica                    | Copia directa sin comprension        | **10%**  |

---


## Bonus de ingenieria (hasta +2.5) {#bonus-de-ingenieria--hasta-plus-2-dot-5}

| **Bonus**         | **Descripcion**                                                         | **Puntos** |
|-------------------|-------------------------------------------------------------------------|------------|
| Sonido de pulso   | Carga y reproduce un efecto de sonido al crear cada `Bala`              | **+0.5**   |
| Fuego en rafaga   | Mantener ESPACIO pulsado dispara automaticamente cada 200ms (cooldown)  | **+1.0**   |
| Municion dinamica | Las balas cambian de color o tamaño gradualmente al alejarse de la nave | **+1.0**   |

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                         | **Donde lo ves**                                                  |
|--------------------------------------|-------------------------------------------------------------------|
| **Herencia de Sprite**               | `class Bala(Sprite):` hereda para poder usar `Group`              |
| **pygame.Rect() sin imagen**         | Construir un rectangulo desde cero con coordenadas y dimensiones  |
| **pygame.draw.rect()**               | Dibujar un rectangulo solido en pantalla (sin imagen, solo color) |
| **pygame.sprite.Group**              | Coleccion de sprites: `update()` y `sprites()` en bloque          |
| **Instanciacion dinamica**           | Cada ESPACIO crea un `Bala(self)` nuevo en tiempo de ejecucion    |
| **Fuga de memoria (balas fantasma)** | Objetos invisibles que siguen consumiendo RAM si no se eliminan   |
| **Iteracion segura con .copy()**     | No puedes borrar de una coleccion mientras la recorres            |
| **Recurso limitado**                 | `balas_permitidas` obliga al jugador a apuntar bien — game design |

---

> _"Disparar es facil. Lo dificil es gestionar lo que disparas."_ -- Cualquier ingeniero de software que ha sufrido una fuga de memoria
