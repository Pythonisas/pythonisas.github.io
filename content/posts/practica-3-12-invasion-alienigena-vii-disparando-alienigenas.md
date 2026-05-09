+++
title = "Practica 3.12 - Invasion Alienigena VII: Disparando a los Alienigenas"
author = ["Jordi"]
tags = ["prácticas"]
url = "/pygame7/"
draft = true
+++

## Mision: El enemigo contraataca {#mision-el-enemigo-contraataca}

**Contexto galactico:** Tus armas funcionan y la flota cae bajo tus disparos. Pero los alienigenas no son estupidos: han aprendido a acercarse. Si uno toca tu nave o llega al fondo de la pantalla, sera catastrofico. Ademas, tu codigo de colisiones crece sin control dentro de un metodo que ya hace demasiadas cosas.

Tres problemas de ingenieria en esta practica:

1.  **Deuda tecnica** — Tu `_actualizar_balas()` se ha convertido en un metodo monstruo: actualiza posiciones, limpia balas viejas, detecta colisiones Y regenera la flota. Cada responsabilidad extra que le añadas lo hara mas fragil. ¿Como lo descompones antes de que sea inmantenible?

2.  **El enemigo como amenaza real** — Los alienigenas se mueven y bajan, pero tu nave es invulnerable. Necesitas dos tipos de deteccion: alien toca la nave (`sprite vs grupo`) y alien llega al fondo (`rect.bottom vs alto_pantalla`). Son problemas similares pero requieren herramientas diferentes

3.  **Testear lo que construyes** — Destruir 50 alienigenas uno a uno para probar la regeneracion es tedioso. Los ingenieros de juegos usan trucos: _balas gigantes_, _balas inmortales_, valores extremos. ¿Como testeas rapido sin romper el juego final?

> Basado en el Capitulo 13 de _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Herramientas a tu disposicion {#herramientas-a-tu-disposicion}

| **Herramienta**                                 | **Para que sirve**                                                      |
|-------------------------------------------------|-------------------------------------------------------------------------|
| `pygame.sprite.spritecollideany(sprite, grupo)` | ¿Algun miembro del grupo toca este sprite? Devuelve el primero o `None` |
| `pygame.sprite.groupcollide(g1, g2, b1, b2)`    | Ya la conoces de P3.11 — grupo contra grupo                             |
| `rect.bottom >` alto_pantalla=                  | Detectar si un sprite ha llegado al fondo                               |
| `ancho_bala = 300`                              | Truco de testing: balas gigantes para barrer la flota en segundos       |
| `groupcollide(balas, aliens, False, True)`      | Bala inmortal que no desaparece al impactar (solo para testing)         |

---


## Desafio 1: Pagar la deuda tecnica {#desafio-1-pagar-la-deuda-tecnica}

Tu `_actualizar_balas()` hace demasiadas cosas. Antes de añadir nada nuevo, refactoriza: extrae la logica de colisiones + regeneracion a `_verificar_colisiones_bala_alienigena()`.

**Resultado esperado:** `_actualizar_balas()` solo gestiona posiciones y limpieza. `_verificar_colisiones_bala_alienigena()` solo gestiona impactos y oleadas nuevas. Cada metodo, una responsabilidad.

**Pregunta de diseño:** ¿por que importa separar esto ahora? Porque en las practicas siguientes vas a añadir puntuacion, vidas y niveles de dificultad. Si todo esta en un metodo gigante, cada cambio rompera algo.

---


## Desafio 2: La caja de herramientas del tester {#desafio-2-la-caja-de-herramientas-del-tester}

Antes de seguir, aprende a testear rapido. Cambia temporalmente `ancho_bala = 300` en `Ajustes` y dispara. Puedes barrer la flota en segundos.

Prueba tambien `groupcollide(self.balas, self.alienigenas, False, True)` — el primer `False` hace que la bala NO desaparezca al impactar. Una bala inmortal que atraviesa toda la flota.

**Diagnostico:** ¿aparece una nueva oleada al vaciar la flota? ¿Las balas viejas matan aliens recien nacidos? Si pasa lo segundo, revisa que llamas a `.empty()` antes de `_crear_flota()`.

> _Restaura `ancho_bala = 3` antes de entregar. Las balas gigantes son para el ingeniero, no para el jugador._

---


## Desafio 3: El enemigo puede hacerte daño {#desafio-3-el-enemigo-puede-hacerte-daño}

Hasta ahora los alienigenas son decorativos. Necesitas detectar dos situaciones de derrota:

**Situacion A — Alien toca la nave:**

Pygame ofrece `spritecollideany(sprite, grupo)` — compara un sprite individual contra todos los miembros de un grupo. Devuelve el primer alien que colisiona, o `None` si ninguno toca.

¿Donde lo colocas? Al final de `_actualizar_alienigenas()`, despues de mover la flota.

**Situacion B — Alien llega al fondo:**

No hay funcion magica para esto. Recorre los alienigenas y comprueba si `rect.bottom >` alto_pantalla=. Si alguno lo cumple, es game over (con `break` para no seguir comprobando).

**Diagnostico:** ejecuta el juego, deja que la flota baje, y comprueba que aparece un mensaje en consola al colisionar o al llegar al fondo.

**Pregunta de comprension:**
&gt; **"¿Cual es la diferencia entre `groupcollide()` y `spritecollideany()`? ¿Cuando usas cada una?"**

---


## Desafio 4: Preparar el terreno — `_nave_alcanzada()` {#desafio-4-preparar-el-terreno-nave-alcanzada}

Los dos puntos de deteccion (alien toca nave, alien llega al fondo) disparan la misma reaccion. En vez de repetir codigo, centraliza la respuesta en un metodo:

```python
def _nave_alcanzada(self):
    """Responde cuando la nave es alcanzada."""
    print("*** ¡Nave alcanzada! ***")
```

¿Por que crear un metodo que solo tiene un `print()`? Porque en la P3.13 ese metodo hara mucho mas: restar una vida, reiniciar la flota, recentrar la nave, pausar. Al tenerlo aislado, solo tendras que expandirlo sin tocar el resto.

Esto se llama el **principio de preparacion**: escribir codigo que sea facil de ampliar, aunque hoy parezca excesivo.

---


## Entrega {#entrega}

```text
PRACTICA3.12/
+-- invasion_alienigena.py   <-- refactorizado y ampliado
+-- ajustes.py               <-- velocidad ajustada, ancho_bala restaurado
+-- nave.py                  <-- sin cambios
+-- bala.py                  <-- sin cambios
+-- alienigena.py            <-- sin cambios
+-- images/
```

Requisitos funcionales:

-   [ ] `_verificar_colisiones_bala_alienigena()` como metodo separado
-   [ ] `spritecollideany()` detecta colision alien-nave
-   [ ] `_verificar_alienigenas_fondo()` detecta alienigenas en el fondo
-   [ ] `_nave_alcanzada()` centraliza la respuesta
-   [ ] `ancho_bala` restaurado a valor normal (no 300)
-   [ ] Todo lo anterior sigue funcionando

---


## Uso etico de la IA {#uso-etico-de-la-ia}

Si usas IA, incluye prompt y explica:

&gt; **"¿Cual es la diferencia entre `groupcollide()` y `spritecollideany()`? ¿Cuando usas cada una?"**

&gt; **"¿Por que creamos `_nave_alcanzada()` ahora si solo tiene un `print()`?"**

---


## Rubrica por competencias {#rubrica-por-competencias}

| **Criterio**                        | **Maestro (9-10)**                                                 | **Aprendiz (6-8)**                                        | **Recluta (0-5)**             | **Peso** |
|-------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------|-------------------------------|----------|
| **Refactorizacion (deuda tecnica)** | Colisiones extraidas a metodo propio, responsabilidad unica        | Funciona pero colisiones aun dentro de \_actualizar_balas | Sin refactorizacion           | **25%**  |
| **Deteccion alien-nave**            | `spritecollideany` funcional, `_nave_alcanzada()` invocado         | Detecta pero sin centralizar respuesta                    | Nave invulnerable             | **25%**  |
| **Deteccion alien-fondo**           | `_verificar_alienigenas_fondo()` con break + `_nave_alcanzada()`   | Detecta pero sin break o sin metodo centralizado          | Sin deteccion de fondo        | **20%**  |
| **Testing y ajustes**               | Evidencia de haber testeado (velocidad ajustada, ancho restaurado) | Ajustes presentes pero sin evidencia de testing           | Valores por defecto sin tocar | **15%**  |
| **Pensamiento critico / IA**        | Explica groupcollide vs spritecollideany, documenta prompts        | Indica IA pero sin explicar diferencias                   | Copia sin comprension         | **15%**  |

---


## Bonus de ingenieria (hasta +2.5) {#bonus-de-ingenieria--hasta-plus-2-dot-5}

| **Bonus**                   | **Descripcion**                                   | **Puntos** |
|-----------------------------|---------------------------------------------------|------------|
| Disparo lateral (PCC 13-5)  | Nave a la izquierda, aliens vienen por la derecha | **+1.5**   |
| Efecto visual al colisionar | La nave parpadea o cambia de color                | **+0.5**   |
| Sonido al impacto           | `pygame.mixer.Sound` al detectar colision         | **+0.5**   |

> En la P3.13 el juego dejara de ser inmortal: vidas, `juego_activo`, reinicio de nave, y Game Over.

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                             | **Donde lo ves**                                                            |
|------------------------------------------|-----------------------------------------------------------------------------|
| **Deuda tecnica**                        | Metodos que crecen sin control — refactorizar antes de que sea tarde        |
| **Responsabilidad unica**                | Cada metodo hace una sola cosa: actualizar, verificar, responder            |
| **spritecollideany()**                   | Sprite individual vs grupo — nave contra flota                              |
| **groupcollide() vs spritecollideany()** | Dos herramientas para dos situaciones: grupo-vs-grupo vs sprite-vs-grupo    |
| **Testing con valores extremos**         | Balas gigantes, balas inmortales — testear rapido sin romper el juego final |
| **Principio de preparacion**             | `_nave_alcanzada()` hoy es un `print()`, mañana gestionara vidas y reinicio |

---

> _"Cuando el enemigo por fin puede hacerte daño, el juego deja de ser un sandbox y empieza a ser un desafio. Ahi es donde nace la tension."_
