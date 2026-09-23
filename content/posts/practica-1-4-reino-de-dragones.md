+++
title = "Práctica 1.4 — Academia Pythonisa IV: Reino de Dragones"
author = ["Jordi"]
tags = ["prácticas"]
url = "/python4/"
draft = true
+++

## Misión: Las dos cuevas {#misión-las-dos-cuevas}

**Contexto mágico:** La Academia organiza su primera **expedición al Reino de Dragones**. Allí, cada dragón vive en su cueva junto a su tesoro. Algunos son amistosos y lo comparten; otros están hambrientos y se comen a quien entre. Delante de ti hay dos cuevas... y no sabes qué dragón vive en cada una.

Hasta ahora tus programas eran una lista de órdenes de arriba abajo. Este juego es el primero que **organizarás en funciones**: pequeños hechizos con nombre que puedes invocar cuando los necesites. Y antes de escribir una sola línea, lo **diseñarás** con un diagrama de flujo.

> Basado en el Capítulo 5 de _Inventa tus propios juegos de computadora con Python_ -- Al Sweigart ([Cap. 5: Reino de dragones](https://github.com/JaquerEspeis/inventar-con-python/blob/master/capitulo5.md))

Así se ve una partida:

```text
Estás en una tierra llena de dragones. Frente a ti
hay dos cuevas. En una de ellas, el dragón es generoso y amigable
y compartirá su tesoro contigo. El otro dragón es codicioso
y está hambriento, y te devorará inmediatamente.

¿A qué cueva quieres entrar? (1 o 2)
1
Te aproximas a la cueva...
Es oscura y espeluznante...
¡Un gran dragón aparece súbitamente frente a ti! Abre sus fauces y...

¡Te engulle de un bocado!
¿Quieres jugar de nuevo? (sí o no)
no
```

---


## Los problemas a resolver {#los-problemas-a-resolver}

1.  **Diseñar antes de programar** — ¿Qué pasos tiene el juego? ¿Dónde hay que decidir? ¿Dónde se vuelve atrás? Un **diagrama de flujo** te responde antes de escribir código

2.  **Organizar en funciones** — Mostrar la introducción, elegir cueva, explorarla... Cada tarea es una función con `def`. El programa principal solo las _invoca_

3.  **Pasar información** — `explorar_cueva()` necesita saber qué cueva has elegido. Se lo das como **argumento**, y ella lo recibe como **parámetro**

4.  **Devolver resultados** — `elegir_cueva()` tiene que _devolver_ la cueva elegida al programa principal. Para eso está `return`

5.  **Validar la entrada** — Si escriben `3` o `patata`, hay que volver a preguntar. Hace falta un `while` con una condición doble: `and`

6.  **¿Dónde vive cada variable?** — Una variable creada dentro de una función _no existe fuera_. Es el **entorno local** frente al **global**

7.  **El suspense** — Un `time.sleep(2)` entre frase y frase convierte un programa en una historia

---


## Herramientas a tu disposición {#herramientas-a-tu-disposición}

| **Herramienta**          | **Para qué sirve**                            |
|--------------------------|-----------------------------------------------|
| `def nombre(parametro):` | Define una función (un hechizo con nombre)    |
| `return valor`           | La función devuelve un valor a quien la llamó |
| `nombre(argumento)`      | Llama (invoca) a la función                   |
| `and`, `or`, `not`       | Combinan condiciones                          |
| `'''...'''`              | Cadena de varias líneas                       |
| `import time`            | Módulo del tiempo                             |
| `time.sleep(segundos)`   | Pausa el programa                             |

**Tablas de verdad** (pruébalas en la Shell):

| **A**   | **B**   | **`A and B`** | **`A or B`** | **`not A`** |
|---------|---------|---------------|--------------|-------------|
| `True`  | `True`  | `True`        | `True`       | `False`     |
| `True`  | `False` | `False`       | `True`       | `False`     |
| `False` | `True`  | `False`       | `True`       | `True`      |
| `False` | `False` | `False`       | `False`      | `True`      |

---


## Desafío 1: Diseña el juego (diagrama de flujo) {#desafío-1-diseña-el-juego--diagrama-de-flujo}

Antes de programar, dibuja el **diagrama de flujo** del juego. Cada caja es una acción; cada flecha, el camino a la siguiente. Donde el camino se divide, hay una **decisión**.

**Requisitos:**

-   Cajas de **Inicio** y **Fin**
-   Todas las acciones: mostrar introducción, elegir cueva, comprobar dragón, ganar/perder, jugar de nuevo
-   La flecha que **vuelve atrás** si la jugadora quiere jugar otra vez
-   La flecha que vuelve atrás si escribe una cueva que no existe (¡esta no está en el libro!)

Hazlo en papel (y fotografíalo) o en [draw.io](https://app.diagrams.net) (y expórtalo a PNG). Cuando lo tengas, compáralo con el del libro:

{{< figure src="/images/p1-4-diagrama-dragones.png" caption="<span class=\"figure-number\">Figure 1: </span>Diagrama de flujo de Reino de Dragones (Al Sweigart, CC BY-NC-SA)" >}}

**Diagnóstico:** pon el dedo en _Inicio_ y sigue las flechas: tu dedo es la ejecución del programa. ¿Puedes llegar a _Fin_ por todos los caminos? ¿Hay algún camino sin salida?

---


## Desafío 2: Completa el código {#desafío-2-completa-el-código}

-   [dragones_incompleto.py](/code/python4/dragones_incompleto.py)

Renómbralo a `dragones.py`. Completa los huecos `___` y `...`:

```python
# dragones.py — Práctica 1.4: Reino de Dragones
# Completa los huecos marcados con ___ y ...
import random
import ___


def mostrar_introduccion():
    print('''Estás en una tierra llena de dragones. Frente a ti
hay dos cuevas. En una de ellas, el dragón es generoso y amigable
y compartirá su tesoro contigo. El otro dragón es codicioso
y está hambriento, y te devorará inmediatamente.''')
    print()


def elegir_cueva():
    cueva = ''
    while cueva != '1' ___ cueva != '2':
        print('¿A qué cueva quieres entrar? (1 o 2)')
        cueva = input()

    ___ cueva


def explorar_cueva(cueva_elegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.___(2)
    print('¡Un gran dragón aparece súbitamente frente a ti! Abre sus fauces y...')
    print()
    time.sleep(2)

    cueva_amigable = random.randint(1, 2)

    if cueva_elegida == ___(cueva_amigable):
        print('¡Te regala su tesoro!')
    else:
        ...


jugar_de_nuevo = 'sí'
while jugar_de_nuevo == 'sí' ___ jugar_de_nuevo == 's':
    mostrar_introduccion()
    numero_de_cueva = ___()
    explorar_cueva(___)

    print('¿Quieres jugar de nuevo? (sí o no)')
    jugar_de_nuevo = input()
```

**Pistas:**

-   En `elegir_cueva()` el bucle debe repetirse mientras la cueva **no sea** 1 **y** **no sea** 2
-   ¿Por qué comparamos con `str(cueva_amigable)` y no con `cueva_amigable` a secas? (Recuerda la P1.2: ¿qué tipo devuelve `input()`?)
-   El `while` final debe seguir si responden `sí` **o** `s`

**Diagnóstico:** escribe `3`, `hola` y una cadena vacía cuando te pregunte la cueva. El juego tiene que volver a preguntar las tres veces. Si acepta el `3`, revisa el `and`.

---


## Desafío 3: El experimento de los entornos {#desafío-3-el-experimento-de-los-entornos}

Añade **temporalmente** al final del programa (fuera de cualquier función):

```python
print(cueva_amigable)
```

Ejecuta. ¿Qué error sale? ¿Por qué, si la variable _existe_ dentro de `explorar_cueva()`?

Ahora prueba lo contrario: dentro de `explorar_cueva()` añade `print(jugar_de_nuevo)`. ¿Funciona? ¿Por qué?

**Diagnóstico:** abre _Ver → Variables_ mientras juegas. Verás que las variables de una función aparecen... y desaparecen cuando la función termina.

Borra estas pruebas antes de entregar y explica lo que has descubierto en `explicacion.md`.

---


## Desafío 4: Tu propio reino {#desafío-4-tu-propio-reino}

Ahora que funciona, hazlo **tuyo**. Elige al menos **una** ampliación y añádela también a tu diagrama de flujo:

-   Una **tercera cueva** (¿con un dragón dormido?)
-   Un **segundo encuentro** si sobrevives (un puente, un acertijo...)
-   Una función `mostrar_tesoro(monedas)` que reciba un parámetro y muestre el tesoro ganado
-   Otra historia completamente distinta con la misma estructura: dos puertas, dos pociones, dos portales...

---


## Entrega {#entrega}

```text
PRACTICA1.4/
+-- dragones.py            <-- el juego completo y ampliado
+-- diagrama_flujo.png     <-- foto o exportación de draw.io (con tu ampliación)
+-- explicacion.md         <-- tus respuestas a "Explica tu código"
```

Súbela al **servidor SFTP del aula** (`put -r PRACTICA1.4`).

Requisitos funcionales:

-   [ ] El juego se organiza en funciones con `def`
-   [ ] `elegir_cueva()` valida la entrada y **devuelve** la cueva con `return`
-   [ ] `explorar_cueva()` recibe la cueva como **parámetro**
-   [ ] Se puede volver a jugar respondiendo `sí` o `s`
-   [ ] Hay pausas con `time.sleep()`
-   [ ] El diagrama de flujo refleja **tu** versión del juego, incluida la ampliación

---


## Explica tu código {#explica-tu-código}

1.  ¿Qué diferencia hay entre _parámetro_ y _argumento_? Señala uno de cada en tu código
2.  ¿Qué pasaría si quitas el `return cueva` de `elegir_cueva()`? Pruébalo
3.  ¿Qué descubriste en el Desafío 3 sobre dónde "viven" las variables?

---


## Rúbrica por competencias {#rúbrica-por-competencias}

| **Criterio**                                | **Hechicería (9-10)**                                            | **Aprendizaje (6-8)**                                | **Iniciación (0-5)**              | **Peso** |
|---------------------------------------------|------------------------------------------------------------------|------------------------------------------------------|-----------------------------------|----------|
| **Diagrama de flujo**                       | Completo, con bucles de repetición y validación, y la ampliación | Correcto pero sin validación o sin ampliación        | Incompleto o sin diagrama         | **20%**  |
| **Funciones (`def`, `return`, parámetros)** | Funciones claras, `return` y parámetros bien usados              | Funciona pero alguna función no devuelve o no recibe | Todo el código fuera de funciones | **30%**  |
| **Bucles y operadores booleanos**           | Validación con `and`, repetición con `or`, sin fallos            | Una de las dos condiciones falla                     | Acepta entradas no válidas        | **15%**  |
| **Entornos global y local**                 | Explica con precisión el experimento del Desafío 3               | Lo prueba pero la explicación es vaga                | No lo realiza                     | **10%**  |
| **Suspense y creatividad**                  | `sleep()` bien dosificado, ampliación original                   | Ampliación mínima                                    | Sin ampliación                    | **15%**  |
| **Explica tu código**                       | Respuestas claras, con pruebas propias                           | Correctas pero sin probar                            | Sin `explicacion.md`              | **10%**  |

---


## Bonus (hasta +2) {#bonus--hasta-plus-2}

| **Bonus**             | **Descripción**                                                              | **Puntos** |
|-----------------------|------------------------------------------------------------------------------|------------|
| Arte ASCII del dragón | El dragón aparece dibujado (usa `r'''...'''`)                                | **+0.5**   |
| Marcador              | Cuenta partidas ganadas y perdidas, y lo muestra al terminar (con f-strings) | **+0.5**   |
| Dragones con carácter | Cada cueva puede tener un dragón distinto, elegido al azar entre varios      | **+1.0**   |

---


## Conceptos clave {#conceptos-clave}

| **Concepto**              | **Dónde lo ves**                                                        |
|---------------------------|-------------------------------------------------------------------------|
| **Diagrama de flujo**     | El mapa del juego antes de programarlo                                  |
| **Sentencia `def`**       | `def elegir_cueva():` crea una función                                  |
| **Llamada a función**     | `elegir_cueva()` la ejecuta                                             |
| **Parámetro / argumento** | `def explorar_cueva(cueva_elegida)` / `explorar_cueva(numero_de_cueva)` |
| **`return`**              | `return cueva` devuelve el valor al programa principal                  |
| **Operadores booleanos**  | `cueva != '1' and cueva != '2'`                                         |
| **Entorno local**         | `cueva_amigable` solo existe dentro de `explorar_cueva()`               |
| **Entorno global**        | `jugar_de_nuevo` existe en todo el programa                             |
| **Cadena multilínea**     | La introducción entre `'''...'''`                                       |
| **`time.sleep()`**        | Pausas para crear suspense                                              |

---

> _"Una función es un hechizo con nombre: lo escribes una vez y lo invocas mil."_
