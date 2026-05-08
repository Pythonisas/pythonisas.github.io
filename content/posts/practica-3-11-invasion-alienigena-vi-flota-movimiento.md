+++
title = "Practica 3.11 - Invasion Alienigena VI: Haciendo que la Flota se Mueva"
author = ["Fénix"]
tags = ["prácticas"]
url = "/pygame6/"
draft = true
+++

## Mision: La flota cobra vida {#mision-la-flota-cobra-vida}

**Contexto galactico:** La flota alienigena llena el cielo, pero esta congelada — como una foto de familia siniestra. La inteligencia de la Resistencia avisa: en cuanto actives sus motores, se moveran en formacion, bajaran al tocar los bordes, y solo tus balas podran detenerlos. Si limpias una oleada, vendra otra. Y otra. Y otra.

Esta practica tiene cuatro problemas de ingenieria que hacen que tu juego pase de "demo estatica" a "juego de verdad":

1.  **Movimiento coordinado** — 50 alienigenas deben moverse juntos. ¿Como haces que TODOS cambien de direccion cuando UNO toca el borde? Pista: una variable que vale `1` o `-1` y se multiplica por la velocidad

2.  **El problema del break** — Si 8 alienigenas tocan el borde a la vez y cada uno dispara un cambio de direccion, la flota baja 8 veces en un solo frame. ¿Como evitas esta reaccion en cadena?

3.  **Colisiones entre grupos** — Tus balas y los alienigenas son dos colecciones de sprites independientes. Necesitas comparar cada bala con cada alien para detectar impactos. ¿Hacerlo a mano con bucles anidados? Pygame tiene algo mejor

4.  **Regeneracion infinita** — Cuando destruyes toda la flota, ¿que pasa? La pantalla queda vacia. Necesitas detectar que el grupo esta vacio y crear una oleada nueva — sin que las balas de la oleada anterior maten aliens recien nacidos

> Basado en el Capitulo 13 de _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Herramientas a tu disposicion {#herramientas-a-tu-disposicion}

| **Herramienta**                              | **Para que sirve**                                         |
|----------------------------------------------|------------------------------------------------------------|
| `direccion_flota = 1` (o `-1`)               | Multiplicador de velocidad: `1` derecha, `-1` izquierda    |
| `rect.right`, `rect.left`                    | Bordes del sprite para detectar limites de pantalla        |
| `pygame.sprite.groupcollide(g1, g2, b1, b2)` | Compara dos grupos rect a rect, elimina los que colisionan |
| `if not grupo:`                              | Python trata colecciones vacias como `False`               |
| `grupo.empty()`                              | Vacia un grupo de sprites de golpe                         |

---


## Desafio 1: Poner la flota en marcha {#desafio-1-poner-la-flota-en-marcha}

Haz que los alienigenas se muevan lateralmente. Todos deben compartir la misma velocidad y direccion — centralizadas en `Ajustes`.

**Requisitos:**

-   `velocidad_alienigena`, `velocidad_caida_flota` y `direccion_flota` en `ajustes.py`
-   `actualizar()` en `Alienigena` que mueva usando `velocidad * direccion`
-   `self.alienigenas.update()` en el game loop

**Diagnostico:** ejecuta el juego. La flota deberia moverse a la derecha... y desaparecer por el borde. Normal: aun no has puesto limites.

---


## Desafio 2: Bordes y cambio de direccion {#desafio-2-bordes-y-cambio-de-direccion}

Cuando **cualquier** alienigena toque un borde, **toda** la flota debe bajar un escalon y cambiar de sentido.

**El problema del break:** si recorres todos los aliens y cada uno que toca el borde dispara un cambio de direccion, la flota baja multiples veces por frame. Necesitas salir del bucle en cuanto detectas el primer alien en el borde.

**Requisitos:**

-   `verificar_bordes()` en `Alienigena` — informa, no actua
-   `_verificar_bordes_flota()` en `InvasionAlienigena` — recorre, detecta, y sale con `break`
-   `_cambiar_direccion_flota()` — baja todos + invierte `direccion_flota *` -1=

**Diagnostico:** la flota deberia rebotar de un lado a otro, bajando un escalon en cada rebote.

---


## Desafio 3: Destruir alienigenas {#desafio-3-destruir-alienigenas}

Tus balas atraviesan la flota sin hacer nada. Necesitas deteccion de colisiones entre dos grupos de sprites.

**Tu mision:** cuando una bala toque un alienigena, ambos desaparecen.

**Pista:** `pygame.sprite.groupcollide(self.balas, self.alienigenas, True, True)` — los dos `True` eliminan tanto la bala como el alien que colisionan. Una linea hace todo el trabajo.

**Pregunta de diseño:** ¿que pasa si pones `False` en vez de `True` para las balas? ¿Y para los aliens? Experimenta y observa la diferencia.

---


## Desafio 4: Oleadas infinitas {#desafio-4-oleadas-infinitas}

Destruye toda la flota. ¿Que pasa? La pantalla queda vacia.

**Tu mision:** cuando el grupo de alienigenas quede vacio, limpia las balas existentes y genera una flota nueva.

**Trampa tecnica:** si no limpias las balas antes de crear la nueva flota, las balas que estaban subiendo mataran aliens recien creados antes de que el jugador los vea. `self.balas.empty()` resuelve esto.

**Diagnostico:** destruye toda la flota. Deberia aparecer una nueva instantaneamente.

---


## Entrega {#entrega}

No hay ficheros nuevos — todo es ampliar los existentes:

```text
PRACTICA3.11/
+-- invasion_alienigena.py   <-- ampliado
+-- ajustes.py               <-- ampliado
+-- alienigena.py            <-- ampliado
+-- nave.py                  <-- sin cambios
+-- bala.py                  <-- sin cambios
+-- images/
```

Requisitos funcionales:

-   [ ] La flota se mueve lateralmente y baja al tocar un borde
-   [ ] Las balas destruyen alienigenas (`groupcollide`)
-   [ ] Al eliminar toda la flota, aparece una nueva oleada
-   [ ] El game loop esta limpio (`_actualizar_alienigenas()` como metodo privado)
-   [ ] Sin reaccion en cadena al tocar bordes (`break` correcto)

---


## Uso etico de la IA {#uso-etico-de-la-ia}

Mismas reglas que P3.9 y P3.10. Si usas IA, incluye prompt y explica:

&gt; **"¿Por que es necesario el `break` en `_verificar_bordes_flota()`? ¿Que pasaria sin el?"**

&gt; **"¿Que significan los dos `True` en `groupcollide()`?"**

---


## Rubrica por competencias {#rubrica-por-competencias}

| **Criterio**                           | **Maestro (9-10)**                                               | **Aprendiz (6-8)**                                       | **Recluta (0-5)**              | **Peso** |
|----------------------------------------|------------------------------------------------------------------|----------------------------------------------------------|--------------------------------|----------|
| **Movimiento coordinado**              | `actualizar()` con velocidad\*direccion, ajustes centralizados   | Se mueve pero direccion hardcodeada o sin ajustes        | No se mueve o sale de pantalla | **25%**  |
| **Bordes y cambio de direccion**       | `verificar_bordes()` + `break` correcto + baja+invierte          | Cambia de direccion pero con bug de reaccion en cadena   | No detecta bordes              | **25%**  |
| **Colisiones bala-alien**              | `groupcollide` funcional, ambos desaparecen                      | Colisiones parciales o solo desaparece uno               | Balas atraviesan aliens        | **20%**  |
| **Regeneracion de oleadas**            | Detecta grupo vacio, limpia balas, crea nueva flota              | Regenera pero sin limpiar balas (aliens mueren al nacer) | Sin regeneracion               | **15%**  |
| **Arquitectura + pensamiento critico** | `_actualizar_alienigenas()` limpio, explica break y groupcollide | Funciona pero game loop desordenado                      | Sin refactorizacion            | **15%**  |

---


## Bonus de ingenieria (hasta +3) {#bonus-de-ingenieria--hasta-plus-3}

| **Bonus**                  | **Descripcion**                                     | **Puntos** |
|----------------------------|-----------------------------------------------------|------------|
| Velocidad progresiva       | Cada oleada nueva incrementa `velocidad_alienigena` | **+0.75**  |
| Sonido al impactar         | `pygame.mixer` al destruir un alien                 | **+0.75**  |
| Oleadas con mas filas      | Cada nueva flota tiene 1 fila extra                 | **+0.5**   |
| Gotas de lluvia (PCC 13-3) | Cuadricula de gotas que cae hasta desaparecer abajo | **+1.0**   |

> En las siguientes practicas los alienigenas podran destruir tu nave y el juego tendra vidas, "Game Over!" y boton de reinicio.

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                     | **Donde lo ves**                                                        |
|----------------------------------|-------------------------------------------------------------------------|
| **Direccion como multiplicador** | `direccion_flota` (1/-1) multiplicada por velocidad invierte el sentido |
| **Deteccion de bordes**          | `verificar_bordes()` compara `rect.right/left` con bordes de pantalla   |
| **El problema del break**        | Sin `break`, multiples aliens en borde = multiples bajadas por frame    |
| **groupcollide()**               | Compara dos grupos rect a rect y elimina los que colisionan             |
| **Regeneracion de contenido**    | `if not grupo:` detecta grupo vacio y dispara `_crear_flota()`          |
| **Limpiar antes de regenerar**   | `.empty()` evita que balas viejas maten aliens nuevos                   |

---

> _"La primera vez que destruyes un alienigena y aparece otra oleada, entiendes el bucle infinito del game design: destruir, crear, repetir."_
