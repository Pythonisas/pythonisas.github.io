+++
title = "Práctica 1.6 — Academia Pythonisa VI: El Ahorcado"
author = ["Jordi"]
tags = ["prácticas"]
url = "/python6/"
draft = true
+++

## Misión: La palabra prohibida {#misión-la-palabra-prohibida}

**Contexto mágico:** En la biblioteca de la Academia hay un libro maldito que solo se abre si alguien adivina su **palabra secreta**, letra a letra. Cada letra equivocada hace aparecer una parte más del ahorcado en la portada... y a la séptima, el libro se cierra para siempre.

Es el **proyecto final del trimestre**, y el programa más largo que has escrito hasta ahora. Por eso lo harás como lo hacen los profesionales: **primero el diseño** (diagrama de flujo), **luego el código** y **finalmente las ampliaciones**.

> Basado en los Capítulos 7, 8 y 9 de _Inventa tus propios juegos de computadora con Python_ -- Al Sweigart ([Cap. 7: Diseño con diagramas de flujo](https://github.com/JaquerEspeis/inventar-con-python/blob/master/capitulo7.md) · [Cap. 8: El código del Ahorcado](https://github.com/JaquerEspeis/inventar-con-python/blob/master/capitulo8.md) · [Cap. 9: Extendiendo el Ahorcado](https://github.com/JaquerEspeis/inventar-con-python/blob/master/capitulo9.md))

Así se ve una partida:

```text
A H O R C A D O

  +---+
      |
      |
      |
     ===

Letras incorrectas:
_ _ _
Adivina una letra.
a
...
  +---+
  O   |
      |
      |
     ===

Letras incorrectas: o
g a _
Adivina una letra.
t
¡Sí! La palabra secreta es "gato". ¡Has ganado!
¿Quieres jugar de nuevo? (sí o no)
```

---


## Los problemas a resolver {#los-problemas-a-resolver}

1.  **El diseño** — Hay bucles dentro de bucles, validaciones, dos formas de terminar (ganar o perder) y la opción de volver a jugar. Sin un mapa, te perderás

2.  **Dibujar el ahorcado** — Siete dibujos de arte ASCII, cada uno de varias líneas. Necesitas guardarlos en **una lista** de cadenas multilínea, y elegir cuál mostrar según los fallos

3.  **Muchas palabras** — Escribir una lista de 60 palabras con comillas y comas es un rollo. `split()` la construye a partir de una sola cadena

4.  **Mostrar `g a _ o`** — Hay que recorrer la palabra letra a letra (bucle `for`) y sustituir cada `_` por la letra acertada. Para eso, **cortes** (`slices`)

5.  **Validar la letra** — ¿Es una sola letra? ¿Ya la había probado? ¿Es un número? Varias condiciones encadenadas: `if` / `elif` / `else`

6.  **¿Ha ganado?** — Hay que comprobar si _todas_ las letras de la palabra están entre las acertadas

---


## Herramientas a tu disposición {#herramientas-a-tu-disposición}

| **Herramienta**               | **Para qué sirve**                                               |
|-------------------------------|------------------------------------------------------------------|
| `r'''...'''`                  | Cadena multilínea _en bruto_ (las `\` del dibujo no son escapes) |
| `MAYUSCULAS = ...`            | Constante: un valor que no debe cambiar                          |
| `[a, b, c]`                   | Lista: varios valores en una sola variable                       |
| `lista[i]`                    | Elemento en la posición `i` (¡se empieza a contar en 0!)         |
| `len(x)`                      | Número de elementos de una lista (o letras de una cadena)        |
| `'a b c'.split()`             | Convierte una cadena en una lista de palabras                    |
| `.lower()` / `.upper()`       | Pasa a minúsculas / mayúsculas                                   |
| `.append()` / `.reverse()`    | Añade al final / da la vuelta a una lista                        |
| `for x in secuencia:`         | Repite el bloque una vez por cada elemento                       |
| `range(n)` / `list(range(n))` | Los números del 0 al `n-1`                                       |
| `cadena[i:j]`                 | Corte: los caracteres desde `i` hasta `j` (sin incluir `j`)      |
| `elif`                        | "Si no, y si..."                                                 |
| `x in y` / `x not in y`       | ¿Está (o no) `x` dentro de `y`?                                  |

---


## Desafío 1: El mapa del libro maldito (diagrama de flujo) {#desafío-1-el-mapa-del-libro-maldito--diagrama-de-flujo}

**Antes de programar**, dibuja el diagrama de flujo del Ahorcado. Constrúyelo por capas, como en el capítulo 7:

1.  Empieza con **Inicio** y **Fin**
2.  Añade las acciones en orden: generar palabra, mostrar tablero, pedir letra
3.  Divide el camino: ¿la letra está en la palabra o no?
4.  Añade las dos formas de terminar: ha adivinado todas las letras / ha agotado los intentos
5.  Añade los **bucles**: volver a pedir letra si el juego no ha terminado, volver a pedirla si ya la había probado, volver a empezar si quiere jugar de nuevo

**Requisitos:**

-   Papel (fotografiado) o [draw.io](https://app.diagrams.net) (exportado a PNG)
-   Tiene que aparecer la ampliación que elijas en el Desafío 3 (puedes completarlo al final)

Cuando lo tengas, compáralo con el del libro. ¿Qué flecha falta en el del libro? (Pista: ¿qué pasa después de "La letra está en la palabra secreta" si _todavía_ no ha ganado?)

{{< figure src="/images/p1-6-diagrama-ahorcado.png" caption="<span class=\"figure-number\">Figure 1: </span>Diagrama de flujo del Ahorcado (Al Sweigart, CC BY-NC-SA)" >}}

---


## Desafío 2: El código del Ahorcado {#desafío-2-el-código-del-ahorcado}

**Primero, un laboratorio de listas.** En la Shell:

```text
>>> animales = 'gato perro buho'.split()
>>> animales
>>> animales[0]
>>> animales[2]
>>> len(animales)
>>> animales.append('dragon')
>>> animales
>>> animales.reverse()
>>> animales
>>> list(range(5))
>>> palabra = 'pythonisa'
>>> palabra[0:6]
>>> palabra[6:]
>>> 'y' in palabra
```

Ahora descarga el fichero incompleto:

-   [ahorcado_incompleto.py](/code/python6/ahorcado_incompleto.py)

Renómbralo a `ahorcado.py`. Completa los huecos `___` y `...`:

```python
# ahorcado.py — Práctica 1.6: El Ahorcado
# Completa los huecos marcados con ___ y ...
import random

IMAGENES_AHORCADO = [r'''
  +---+
      |
      |
      |
     ===''', r'''
  +---+
  O   |
      |
      |
     ===''', r'''
  +---+
  O   |
  |   |
      |
     ===''', r'''
  +---+
  O   |
 /|   |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
      |
     ===''', r'''
  +---+
  O   |
 /|\  |
 /    |
     ===''', r'''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

PALABRAS = ('hormiga babuino tejon murcielago oso castor camello gato cobra '
            'coyote cuervo ciervo perro burro pato aguila zorro rana cabra '
            'ganso halcon leon lagarto llama topo mono raton mula nutria buho '
            'panda loro paloma piton conejo rata salmon foca tiburon oveja '
            'mofeta serpiente cisne tigre sapo trucha pavo tortuga ballena '
            'lobo cebra').___()


def obtener_palabra_al_azar(lista_de_palabras):
    # Devuelve una palabra al azar de la lista.
    indice = random.randint(0, ___(lista_de_palabras) - 1)
    return lista_de_palabras[___]


def mostrar_tablero(letras_incorrectas, letras_correctas, palabra_secreta):
    print(IMAGENES_AHORCADO[len(letras_incorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in ___:
        print(letra, end=' ')
    print()

    espacios = '_' * len(palabra_secreta)

    # Sustituye cada '_' por la letra acertada (¡cortes!)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] in letras_correctas:
            espacios = espacios[:i] + palabra_secreta[i] + espacios[___:]

    # Muestra la palabra con un espacio entre letras
    for letra in espacios:
        print(letra, end=' ')
    print()


def obtener_intento(letras_probadas):
    # Devuelve la letra introducida. Comprueba que sea UNA letra nueva.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.___()
        if len(intento) != 1:
            print('Por favor, introduce una sola letra.')
        ___ intento in letras_probadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor, introduce una LETRA.')
        else:
            return ___


def jugar_de_nuevo():
    # Devuelve True si quiere volver a jugar y False si no.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith(___)


print('A H O R C A D O')
letras_incorrectas = ''
letras_correctas = ''
palabra_secreta = obtener_palabra_al_azar(PALABRAS)
juego_terminado = False

while True:
    mostrar_tablero(letras_incorrectas, letras_correctas, palabra_secreta)

    intento = obtener_intento(letras_incorrectas + letras_correctas)

    if intento in palabra_secreta:
        letras_correctas = letras_correctas + intento

        # ¿Ha encontrado todas las letras?
        encontradas_todas = True
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letras_correctas:
                encontradas_todas = ___
                break
        if encontradas_todas:
            print(f'¡Sí! La palabra secreta es "{palabra_secreta}". ¡Has ganado!')
            juego_terminado = True
    else:
        letras_incorrectas = letras_incorrectas + intento

        # ¿Se ha quedado sin intentos?
        if len(letras_incorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrar_tablero(letras_incorrectas, letras_correctas, palabra_secreta)
            print(f'¡Te has quedado sin intentos! La palabra era "{palabra_secreta}".')
            juego_terminado = ___

    if juego_terminado:
        if jugar_de_nuevo():
            ...   # Reinicia las letras y elige otra palabra secreta
        else:
            ___
```

**Pistas:**

-   En `espacios[:i] + palabra_secreta[i] + espacios[___:]`, quieres _todo lo de antes_ de la posición `i`, la letra nueva y _todo lo de después_. ¿Desde qué posición empieza "lo de después"?
-   ¿Por qué el juego termina cuando hay `len(IMAGENES_AHORCADO) - 1` fallos y no `len(IMAGENES_AHORCADO)`? Cuenta los dibujos
-   El `while True:` del final es un bucle infinito a propósito. ¿Qué palabra lo rompe?

**Diagnóstico:** usa el depurador (`Ctrl+F5`) con un punto de interrupción dentro de `mostrar_tablero()` y observa cómo cambia `espacios` en cada vuelta del `for`. Es la mejor forma de _ver_ los cortes funcionando.

---


## Desafío 3: Extiende el Ahorcado {#desafío-3-extiende-el-ahorcado}

El juego funciona. Ahora conviértelo en **tu** libro maldito. Tienes que hacer **al menos dos** de estas tres ampliaciones:


### A) Categorías con un diccionario {#a-categorías-con-un-diccionario}

Un **diccionario** guarda parejas _clave: valor_. En vez de una lista de palabras, usa una lista por categoría:

```python
PALABRAS = {
    'Colores': 'rojo naranja amarillo verde azul violeta'.split(),
    'Frutas': 'manzana pera sandia uva cereza mango fresa'.split(),
    'Hechizos': ...,   # ¡inventa tu propia categoría!
}
```

Modifica `obtener_palabra_al_azar()` para que:

1.  Elija una **categoría** al azar con `random.choice(list(diccionario.keys()))`
2.  Elija una **palabra** al azar de esa categoría con `random.choice(...)`
3.  Devuelva _las dos cosas_: `return [palabra, categoria]`

Y recíbelas con una **asignación múltiple**:

```python
palabra_secreta, categoria = obtener_palabra_al_azar(PALABRAS)
```

Muestra la categoría como pista en cada turno.


### B) Niveles de dificultad con `elif` {#b-niveles-de-dificultad-con-elif}

Pregunta al principio: `F` (fácil), `M` (medio) o `D` (difícil). Según la respuesta, el juego da más o menos intentos. Pistas:

-   Añade 2 dibujos más a `IMAGENES_AHORCADO` para el nivel fácil (¿un ojo? ¿los dos?)
-   Con `del IMAGENES_AHORCADO[n]` puedes _quitar_ dibujos para los niveles más difíciles
-   Usa `if` / `elif` / `else` para decidir


### C) Tu propio ahorcado {#c-tu-propio-ahorcado}

Cambia el tema entero: otro dibujo ASCII (una poción que se vacía, un castillo que se derrumba, una nave que se aleja...), otras palabras y otros mensajes. Tiene que seguir funcionando con la misma lógica.

**Diagnóstico:** después de cada ampliación, juega al menos una partida completa ganando y otra perdiendo. Si falla, depura: ¿qué valor tienen `palabra_secreta` y `categoria` después de la asignación múltiple?

---


## Entrega {#entrega}

```text
PRACTICA1.6/
+-- ahorcado.py            <-- el juego completo con tus ampliaciones
+-- diagrama_flujo.png     <-- tu diagrama (incluyendo las ampliaciones)
+-- explicacion.md         <-- tus respuestas a "Explica tu código"
```

Súbela al **servidor SFTP del aula** (`put -r PRACTICA1.6`).

Requisitos funcionales:

-   [ ] El diagrama de flujo es tuyo y refleja tu versión del juego
-   [ ] El tablero muestra el dibujo, las letras incorrectas y la palabra con huecos
-   [ ] No se puede repetir una letra ni introducir algo que no sea una letra
-   [ ] Se detecta la victoria y la derrota
-   [ ] Se puede volver a jugar con una palabra nueva
-   [ ] Al menos dos ampliaciones del Desafío 3

---


## Explica tu código {#explica-tu-código}

1.  Explica con un ejemplo qué hace `espacios[:i] + palabra_secreta[i] + espacios[i + 1:]` cuando la palabra es `"gato"` e `i` vale `1`
2.  ¿Por qué `IMAGENES_AHORCADO` está en mayúsculas? ¿Qué pasaría si el programa la modificara sin querer?
3.  ¿Qué diferencia hay entre una _lista_ y un _diccionario_? ¿Cuándo usarías cada uno?

---


## Rúbrica por competencias {#rúbrica-por-competencias}

| **Criterio**                                     | **Hechicería (9-10)**                                        | **Aprendizaje (6-8)**                           | **Iniciación (0-5)**              | **Peso** |
|--------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------|-----------------------------------|----------|
| **Diagrama de flujo**                            | Completo, todos los bucles, incluye las ampliaciones         | Correcto pero le faltan bucles o ampliaciones   | Copia del libro o sin diagrama    | **15%**  |
| **Listas, cadenas y métodos**                    | `split()`, índices, `len()`, `lower()` usados con soltura    | Funciona pero con algún índice fuera de rango   | No construye la lista de palabras | **20%**  |
| **Bucles `for` y cortes**                        | Tablero correcto con cortes; entiende el `for` con `range()` | Tablero correcto con pequeños fallos de formato | El tablero no muestra las letras  | **20%**  |
| **Validación con `if=/=elif=/=else`**            | Rechaza repeticiones, cadenas largas y no-letras             | Alguna validación falla                         | Sin validación                    | **15%**  |
| **Ampliaciones (diccionario, dificultad, tema)** | Dos o más, bien integradas, con asignación múltiple          | Una ampliación completa                         | Ninguna ampliación                | **20%**  |
| **Explica tu código**                            | Respuestas claras, con ejemplos propios                      | Correctas pero sin ejemplos                     | Sin `explicacion.md`              | **10%**  |

---


## Bonus (hasta +2.5) {#bonus--hasta-plus-2-dot-5}

| **Bonus**             | **Descripción**                                                              | **Puntos** |
|-----------------------|------------------------------------------------------------------------------|------------|
| Las tres ampliaciones | Categorías + dificultad + tema propio                                        | **+1.0**   |
| Marcador de partidas  | Cuenta victorias y derrotas entre partidas y las muestra al salir            | **+0.5**   |
| Palabras con tildes   | El juego acepta palabras como `dragón` y la letra `o` acierta también la `ó` | **+1.0**   |

---


## Conceptos clave {#conceptos-clave}

| **Concepto**             | **Dónde lo ves**                                                   |
|--------------------------|--------------------------------------------------------------------|
| **Diagrama de flujo**    | El diseño completo antes de programar                              |
| **Cadena multilínea**    | Cada dibujo entre `r'''...'''`                                     |
| **Constante**            | `IMAGENES_AHORCADO`, `PALABRAS`: en mayúsculas, no se modifican    |
| **Lista e índices**      | `IMAGENES_AHORCADO[len(letras_incorrectas)]`                       |
| **Métodos**              | `.split()`, `.lower()`, `.startswith()`, `.append()`, `.reverse()` |
| **`range()` y `list()`** | `for i in range(len(palabra_secreta)):`                            |
| **Bucle `for`**          | `for letra in letras_incorrectas:`                                 |
| **Cortes (slices)**      | `espacios[:i] + palabra_secreta[i] + espacios[i + 1:]`             |
| **`elif`**               | Validación de la letra en `obtener_intento()`                      |
| **Diccionario**          | `{'Colores': [...], 'Frutas': [...]}`                              |
| **`random.choice()`**    | Elige un elemento al azar de una lista                             |
| **Asignación múltiple**  | `palabra_secreta, categoria = obtener_palabra_al_azar(PALABRAS)`   |

---

> _"Primero el mapa, después el camino. La que diseña antes de programar no se pierde en el bosque de los bucles."_
