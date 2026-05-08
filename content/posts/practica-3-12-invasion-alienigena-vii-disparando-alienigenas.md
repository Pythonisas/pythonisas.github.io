+++
title = "Practica 3.12 - Invasion Alienigena VII: Disparando a los Alienigenas"
author = ["Jordi"]
tags = ["prácticas"]
url = "/pygame7/"
draft = true
+++

## Objetivo {#objetivo}

Tu flota se mueve y tus balas destruyen alienigenas, pero el codigo de colisiones esta metido dentro de `_actualizar_balas()` y crece sin control. Ademas, los alienigenas son inofensivos: aunque lleguen a tu nave, no pasa nada.

En esta practica vas a:

-   Refactorizar el codigo de colisiones en su propio metodo
-   Aprender a ajustar velocidades para mejorar la jugabilidad
-   Usar un truco de _balas gigantes_ para testear mas rapido
-   Detectar cuando un alienigena alcanza tu nave (`spritecollideany`)
-   Detectar cuando un alienigena llega al fondo de la pantalla

Al terminar, tu juego reaccionara cuando un alienigena toque la nave o llegue abajo. Todavia no habra "Game Over" (eso sera la P3.13), pero el juego ya distingue entre ganar y perder.

> Basado en el Capitulo 13 de _Python Crash Course, 3rd Edition_ -- Eric Matthes

---


## Punto de partida {#punto-de-partida}

Tu P3.11 funcional: flota que se mueve, balas que destruyen alienigenas, y nueva oleada al vaciar la flota.

```text
PRACTICA3.12/
+-- invasion_alienigena.py   <-- tu P3.11 (vas a refactorizar y ampliar)
+-- ajustes.py               <-- tu P3.11 (vas a ajustar velocidad)
+-- nave.py                  <-- tu P3.11 (sin cambios)
+-- bala.py                  <-- tu P3.11 (sin cambios)
+-- alienigena.py            <-- tu P3.11 (sin cambios)
+-- images/
    +-- nave.bmp
    +-- alienigena.bmp
```

---


## Paso 1 -- Refactorizar: `_verificar_colisiones_bala_alienigena()` {#paso-1-refactorizar-verificar-colisiones-bala-alienigena}

En la P3.11, la deteccion de colisiones y la regeneracion de la flota estan dentro de `_actualizar_balas()`. Ese metodo ya hace demasiadas cosas: actualiza posiciones, elimina balas viejas, detecta colisiones y regenera la flota. Vamos a extraer la logica de colisiones a su propio metodo:

```python
def _actualizar_balas(self):
    """Actualiza la posicion de las balas y elimina las antiguas."""
    self.balas.update()

    # Eliminar balas que han salido de pantalla
    for bala in self.balas.copy():
        if bala.rect.bottom <= 0:
            self.balas.remove(bala)

    self._verificar_colisiones_bala_alienigena()

def _verificar_colisiones_bala_alienigena(self):
    """Responde a colisiones entre balas y alienigenas."""
    # Eliminar balas y alienigenas que han colisionado
    colisiones = pygame.sprite.groupcollide(
        self.balas, self.alienigenas, True, True)

    if not self.alienigenas:
        # Destruir balas existentes y crear nueva flota
        self.balas.empty()
        self._crear_flota()
```

Ahora `_actualizar_balas()` hace una sola cosa: gestionar la posicion de las balas. Y `_verificar_colisiones_bala_alienigena()` se encarga de las colisiones y la regeneracion. Cada metodo tiene una responsabilidad clara.

¿Por que importa esto? Porque en las siguientes practicas vas a añadir mas logica (puntuacion, vidas, nivel de dificultad). Si todo esta en un solo metodo gigante, sera imposible de mantener.

---


## Paso 2 -- Ajustar la velocidad de las balas {#paso-2-ajustar-la-velocidad-de-las-balas}

La velocidad de las balas afecta directamente a la jugabilidad. Si son demasiado lentas, el juego frustra. Si son demasiado rapidas, no hay desafio.

En `ajustes.py`, ajusta `velocidad_bala` hasta encontrar un valor que te guste:

```python
# Ajustes de balas
self.velocidad_bala = 2.5
self.ancho_bala = 3
self.alto_bala = 15
self.color_bala = (60, 60, 60)
self.balas_permitidas = 3
```

Prueba con `2.0`, `2.5` y `3.0`. El valor perfecto depende de tu pantalla y de tu gusto. Recuerda que el juego se ira acelerando en practicas futuras, asi que no lo hagas demasiado facil al principio.

---


## Paso 3 -- Truco: balas gigantes para testear {#paso-3-truco-balas-gigantes-para-testear}

Probar que la regeneracion de la flota funciona es tedioso si tienes que destruir decenas de alienigenas uno a uno. Hay un truco: haz las balas enormes temporalmente.

En `ajustes.py`, cambia el ancho:

```python
self.ancho_bala = 300  # Solo para testear!
```

Con balas de 300 pixeles de ancho, puedes barrer la flota en segundos y comprobar que aparece una nueva oleada. Tambien puedes probar con `3000` para eliminar la flota de un solo disparo.

{{< figure src="/images/balas-gigantes-test.png" >}}

> _Recuerda restaurar `self.ancho_bala = 3` cuando termines de testear. No entregues el juego con balas gigantes!_

Tambien puedes combinar con el primer argumento `False` de `groupcollide()` para crear una _bala superpoderosa_ que atraviesa toda la pantalla sin desaparecer:

```python
# Bala que NO desaparece al colisionar (solo para testing)
colisiones = pygame.sprite.groupcollide(
    self.balas, self.alienigenas, False, True)
```

---


## Paso 4 -- Detectar colision alien-nave {#paso-4-detectar-colision-alien-nave}

Hasta ahora, los alienigenas son decorativos: se mueven, bajan, pero no pueden hacerte daño. Vamos a cambiar eso.

Pygame ofrece `spritecollideany()` para comprobar si un sprite individual ha colisionado con algun miembro de un grupo. Añade esta comprobacion al final de `_actualizar_alienigenas()`:

```python
def _actualizar_alienigenas(self):
    """Verifica bordes y actualiza posiciones de toda la flota."""
    self._verificar_bordes_flota()
    self.alienigenas.update()

    # Detectar colision alien-nave
    if pygame.sprite.spritecollideany(self.nave, self.alienigenas):
        print("*** ¡Nave alcanzada! ***")
```

`spritecollideany()` recibe dos argumentos:

-   Un sprite individual (`self.nave`)
-   Un grupo de sprites (`self.alienigenas`)

Recorre el grupo y devuelve el primer alienigena que colisiona con la nave. Si ninguno colisiona, devuelve `None`. Como `None` es _falsy_, el `if` solo se activa cuando hay colision.

Ejecuta el juego, deja que los alienigenas bajen hasta tu nave y comprueba que aparece `*** ¡Nave alcanzada! ***` en la terminal.

¿Cual es la diferencia con `groupcollide()`?

-   `groupcollide()`: compara **grupo contra grupo** (balas vs alienigenas)
-   `spritecollideany()`: compara **un sprite contra un grupo** (nave vs alienigenas)

---


## Paso 5 -- Detectar alienigenas que llegan al fondo {#paso-5-detectar-alienigenas-que-llegan-al-fondo}

Un alienigena no necesita tocar tu nave para ser una amenaza. Si un alienigena llega al fondo de la pantalla, tambien deberia contar como un impacto.

Añade un metodo que compruebe si algun alienigena ha llegado abajo:

```python
def _verificar_alienigenas_fondo(self):
    """Comprueba si algun alienigena ha llegado al fondo de la pantalla."""
    for alienigena in self.alienigenas.sprites():
        if alienigena.rect.bottom >= self.ajustes.alto_pantalla:
            # Tratar como si la nave hubiera sido alcanzada
            print("*** ¡Alienigena llego al fondo! ***")
            break
```

Llama a este metodo desde `_actualizar_alienigenas()`:

```python
def _actualizar_alienigenas(self):
    """Verifica bordes y actualiza posiciones de toda la flota."""
    self._verificar_bordes_flota()
    self.alienigenas.update()

    # Detectar colision alien-nave
    if pygame.sprite.spritecollideany(self.nave, self.alienigenas):
        print("*** ¡Nave alcanzada! ***")

    # Detectar alienigenas que llegan al fondo
    self._verificar_alienigenas_fondo()
```

Ahora el juego detecta dos condiciones de derrota: alienigena toca la nave, o alienigena llega al fondo. Por ahora solo imprimimos un mensaje. En la P3.13 añadiremos vidas, reinicio y Game Over.

---


## Paso 6 -- Crear `_nave_alcanzada()` (preparando el terreno) {#paso-6-crear-nave-alcanzada--preparando-el-terreno}

Los dos `print()` que acabas de añadir hacen lo mismo: responder a una situacion en la que el jugador "pierde". En vez de repetir la logica, vamos a crear un metodo dedicado:

```python
def _nave_alcanzada(self):
    """Responde a la nave siendo alcanzada por un alienigena."""
    print("*** ¡Nave alcanzada! ***")
```

Ahora sustituye los dos `print()` por llamadas a `_nave_alcanzada()`:

```python
def _actualizar_alienigenas(self):
    """Verifica bordes y actualiza posiciones de toda la flota."""
    self._verificar_bordes_flota()
    self.alienigenas.update()

    # Detectar colision alien-nave
    if pygame.sprite.spritecollideany(self.nave, self.alienigenas):
        self._nave_alcanzada()

    # Detectar alienigenas que llegan al fondo
    self._verificar_alienigenas_fondo()

def _verificar_alienigenas_fondo(self):
    """Comprueba si algun alienigena ha llegado al fondo."""
    for alienigena in self.alienigenas.sprites():
        if alienigena.rect.bottom >= self.ajustes.alto_pantalla:
            self._nave_alcanzada()
            break
```

¿Por que crear un metodo que solo tiene un `print()`? Porque en la P3.13 ese metodo hara mucho mas: restar una vida, reiniciar la flota, recentrar la nave, y pausar brevemente. Al tenerlo ya aislado, solo tendras que expandir `_nave_alcanzada()` sin tocar el resto del codigo.

---


## Entrega {#entrega}

-   [ ] `invasion_alienigena.py` -- `_verificar_colisiones_bala_alienigena()` como metodo separado
-   [ ] `invasion_alienigena.py` -- `spritecollideany()` detecta colision alien-nave
-   [ ] `invasion_alienigena.py` -- `_verificar_alienigenas_fondo()` detecta alienigenas en el fondo
-   [ ] `invasion_alienigena.py` -- `_nave_alcanzada()` centraliza la respuesta
-   [ ] `ajustes.py` -- `velocidad_bala` ajustada (valor razonable, no gigante)
-   [ ] El juego imprime mensajes al colisionar o llegar al fondo
-   [ ] `ancho_bala` restaurado a valor normal (no 300)
-   [ ] Todo lo anterior (movimiento, balas, flota) sigue funcionando

&gt;    RECORDATORIO: organiza las entregas por carpetas (P3.6 a P3.12)

---


## BONUS -- Para nota maxima {#bonus-para-nota-maxima}

| **Bonus**                         | **Descripcion**                                                                          | **Puntos** |
|-----------------------------------|------------------------------------------------------------------------------------------|------------|
| Disparo lateral (13-5)            | Adaptar el juego para que la nave este a la izquierda y los aliens vengan por la derecha | **+1.5**   |
| Efecto visual al colisionar       | La nave parpadea o cambia de color al ser alcanzada                                      | **+0.5**   |
| Sonido al impacto nave-alien      | `pygame.mixer.Sound` al detectar colision                                                | **+0.5**   |
| Marcador de alienigenas restantes | Mostrar en terminal cuantos alienigenas quedan en la oleada actual                       | **+0.25**  |

> El ejercicio 13-5 es el _TRY IT YOURSELF_ del libro para esta seccion. Intentarlo es la mejor forma de consolidar lo aprendido.

<!--quoteend-->

> En la P3.13 añadiremos vidas, la bandera `juego_activo`, reinicio de nave, pausa entre oleadas y Game Over. El juego dejara de ser inmortal.

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                             | **Donde lo ves**                                                          |
|------------------------------------------|---------------------------------------------------------------------------|
| **Refactorizacion: extraer metodo**      | `_verificar_colisiones_bala_alienigena()` nace de `_actualizar_balas()`   |
| **Responsabilidad unica**                | Cada metodo hace una sola cosa: actualizar, verificar, responder          |
| **spritecollideany()**                   | Compara un sprite individual contra un grupo (nave vs flota)              |
| **groupcollide() vs spritecollideany()** | Grupo-vs-grupo vs sprite-vs-grupo: dos herramientas para dos situaciones  |
| **Testing con valores extremos**         | `ancho_bala = 300` para probar regeneracion de flota rapidamente          |
| **Preparar para el futuro**              | `_nave_alcanzada()` empieza con `print()` pero esta listo para expandirse |

---


## Rubrica {#rubrica}

| **Criterio**                                                        | **Puntos** |
|---------------------------------------------------------------------|------------|
| Refactorizacion: `_verificar_colisiones_bala_alienigena()` separado | 2          |
| `spritecollideany()` detecta colision alien-nave                    | 2          |
| `_verificar_alienigenas_fondo()` detecta alienigenas en el fondo    | 2          |
| `_nave_alcanzada()` centraliza la respuesta                         | 1          |
| `ajustes.py` -- velocidad de balas ajustada, ancho restaurado       | 1          |
| Ejecucion (todo funciona, mensajes aparecen en terminal)            | 2          |
| **Total base**                                                      | **10**     |
| BONUS (hasta +2.75, max 10)                                         | +2.75      |

---

> _"Cuando el enemigo por fin puede hacerte daño, el juego deja de ser un sandbox y empieza a ser un desafio. Ahi es donde nace la tension."_
