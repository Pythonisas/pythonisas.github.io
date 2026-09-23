+++
title = "Práctica 1.2 — Academia Pythonisa II: Adivina el Número"
author = ["Jordi"]
date = 2026-09-21T10:05:00+02:00
tags = ["prácticas"]
url = "/python2/"
draft = false
+++

## Misión: La esfera adivinatoria {#misión-la-esfera-adivinatoria}

**Contexto mágico:** En el aula de Adivinación hay una esfera de cristal que _piensa_ un número secreto entre 1 y 20. Quien quiera consultarla tiene **seis intentos** para acertarlo. Después de cada intento, la esfera brilla en rojo (_demasiado alto_) o en azul (_demasiado bajo_). La esfera se ha estropeado, y te toca a ti construir una nueva... en Python.

Es tu primer **juego** de verdad. Un programa corto, pero con todos los ingredientes de uno grande: azar, repetición, decisiones y datos que escribe la persona que juega.

> Basado en el Capítulo 3 de _Inventa tus propios juegos de computadora con Python_ -- Al Sweigart ([Cap. 3: Adivina el número](https://github.com/JaquerEspeis/inventar-con-python/blob/master/capitulo3.md))

Así se ve una partida (lo que escribe la jugadora va en **negrita**):

```text
¡Hola! ¿Cómo te llamas?
Ada
Bueno, Ada, estoy pensando en un número entre 1 y 20.
Intenta adivinar.
10
Tu estimación es muy alta.
Intenta adivinar.
2
Tu estimación es muy baja.
Intenta adivinar.
4
¡Buen trabajo, Ada! Has adivinado mi número en 3 intentos.
```

---


## Los problemas a resolver {#los-problemas-a-resolver}

1.  **El azar** — Python no trae de serie la magia de los números aleatorios: está guardada en un _módulo_ llamado `random`. Hay que **importarlo** antes de usarlo

2.  **Repetir** — Pedir un número, comprobarlo, volver a pedir... hasta seis veces. No vas a copiar el mismo código seis veces: necesitas un **bucle** `while`

3.  **Los tipos de datos** — `input()` siempre devuelve **texto**. Y para Python, `'4'` (texto) y `4` (número) **no son lo mismo**: no puedes comparar `< 4` con una cadena. Hay que **convertir**

4.  **Decidir** — ¿Muy alto? ¿Muy bajo? ¿Acierto? Cada caso necesita una **condición** y una sentencia `if`

5.  **Salir antes de tiempo** — Si aciertas al segundo intento, no tiene sentido seguir preguntando. Necesitas **romper** el bucle con `break`

---


## Herramientas a tu disposición {#herramientas-a-tu-disposición}

| **Herramienta**                       | **Para qué sirve**                                            |
|---------------------------------------|---------------------------------------------------------------|
| `import random`                       | Trae el módulo de números aleatorios a tu programa            |
| `random.randint(1, 20)`               | Devuelve un entero al azar entre 1 y 20 (_ambos incluidos_)   |
| `while condicion:`                    | Repite el bloque de debajo _mientras_ la condición sea `True` |
| `if condicion:`                       | Ejecuta el bloque de debajo _solo si_ la condición es `True`  |
| `< > <= >= == !=`                     | Comparan dos valores y devuelven `True` o `False`             |
| `int()`, `float()`, `str()`, `bool()` | Convierten un valor a otro tipo                               |
| `break`                               | Sale del bucle inmediatamente                                 |

---


## Tu taller: ahora sí, Thonny {#tu-taller-ahora-sí-thonny}

La consola interactiva está muy bien para probar cosas sueltas, pero este juego ya tiene varias líneas que se repiten y se anidan. A partir de aquí usaremos **Thonny** con **Python 3.11**: un editor pensado para aprender, con depurador incorporado (lo estrenarás en la P1.5) y sin configuraciones raras.

| **Zona / atajo**    | **Para qué sirve**                                                         |
|---------------------|----------------------------------------------------------------------------|
| **Editor** (arriba) | Donde escribes tus programas `.py`                                         |
| **Shell** (abajo)   | La misma consola interactiva de la P1.1: el símbolo `>>>` espera órdenes   |
| `F5` o botón ▶      | Ejecuta el programa del editor                                             |
| `Ctrl+S`            | Guarda el fichero (Thonny te pedirá nombre la primera vez)                 |
| `Ctrl+O`            | Abre un fichero guardado                                                   |
| _Ver → Variables_   | Muestra una tabla con todas tus variables y sus valores. **¡Actívalo ya!** |

💡 ¿Qué versión de Python usa tu Thonny? Escribe en la Shell: `import sys` y después `sys.version`.

---


## Antes de empezar: bloques y sangría {#antes-de-empezar-bloques-y-sangría}

En Python, los **bloques** de código se marcan con la **sangría**: los espacios al principio de la línea. Todo lo que tiene 4 espacios después de un `while` o un `if` _pertenece_ a él. Cuando la sangría vuelve atrás, el bloque termina.

```text
while intentos_realizados < 6:        <-- empieza el bloque del while
....estimacion = int(input())
....if estimacion < numero_secreto:   <-- empieza el bloque del if
........print('Muy baja.')
....if estimacion == numero_secreto:
........break
print('Fin del juego')                <-- ya estamos fuera del while
```

Thonny pone la sangría automáticamente cuando pulsas Enter después de `:`. Para **salir** del bloque, borra los espacios con la tecla de retroceso.

⚠️ La diferencia entre `=` y `==`: `=` **guarda** (`numero = 5`), `==` **pregunta** (`numero == 5` → `True` o `False`). Es el error más típico de este trimestre.

---


## Descarga el fichero incompleto {#descarga-el-fichero-incompleto}

-   [adivina_incompleto.py](/code/python2/adivina_incompleto.py)

Renómbralo a `adivina_el_numero.py`. Completa los huecos marcados con `___` y `...`:

```python
# adivina_el_numero.py — Práctica 1.2: La esfera adivinatoria
# Completa los huecos marcados con ___ y ...
import ___

intentos_realizados = 0

print('¡Hola! ¿Cómo te llamas?')
mi_nombre = ___()

numero_secreto = random.___(1, 20)
print('Bueno, ' + mi_nombre + ', estoy pensando en un número entre 1 y 20.')

while intentos_realizados < ___:
    print('Intenta adivinar.')
    estimacion = input()
    estimacion = ___(estimacion)   # ¿Por qué hace falta esta línea?

    intentos_realizados = intentos_realizados + 1

    if estimacion < numero_secreto:
        print('Tu estimación es muy baja.')

    if estimacion ___ numero_secreto:
        print('Tu estimación es muy alta.')

    if estimacion == numero_secreto:
        ___

if estimacion == numero_secreto:
    intentos_realizados = ___(intentos_realizados)
    print('¡Buen trabajo, ' + mi_nombre + '! Has adivinado mi número en ' +
          intentos_realizados + ' intentos.')

if estimacion ___ numero_secreto:
    ...   # Muestra cuál era el número secreto
```

---


## Desafío 1: La esfera piensa {#desafío-1-la-esfera-piensa}

Antes de construir el juego entero, asegúrate de que la esfera sabe **pensar un número**.

**Requisitos:**

-   Completa el `import` y la llamada a `random.randint()`
-   Añade **temporalmente** `print(numero_secreto)` justo después, para ver qué número ha pensado
-   Ejecuta el programa varias veces: ¿sale siempre un número distinto? ¿Alguna vez sale el 1 o el 20?

**Diagnóstico:** si te aparece `NameError: name 'random' is not defined`, te falta el `import` (o está después de usarlo: el `import` va arriba del todo).

💡 Ese `print(numero_secreto)` es un **truco de depuración**: te deja ver lo que el programa esconde. Déjalo mientras pruebas y **bórralo** antes de entregar... o la esfera no tendrá ningún misterio.

---


## Desafío 2: El bucle de intentos {#desafío-2-el-bucle-de-intentos}

Haz que la esfera te deje intentarlo **hasta seis veces** y te diga si vas alta o baja.

**Primero, un laboratorio de conversiones.** En la Shell, prueba y apunta qué pasa:

```text
>>> '4' == 4
>>> int('4') == 4
>>> int('42') + 8
>>> float('3.5')
>>> str(7) + '7'
>>> bool(0)
>>> bool('hola')
>>> int('hola')
```

**Requisitos:**

-   Completa la condición del `while` para que se repita 6 veces como máximo
-   Convierte `estimacion` a número entero antes de compararla
-   Completa el operador que falta para "muy alta"

**Diagnóstico:** si te sale `TypeError: '<' not supported between instances of 'str' and 'int'`, Python te está diciendo que intentas comparar un texto con un número. ¿Qué línea convierte el texto en número?

---


## Desafío 3: El veredicto final {#desafío-3-el-veredicto-final}

Cuando la jugadora acierte, el bucle debe **terminar enseguida**. Y al salir, la esfera tiene que dar su veredicto.

**Requisitos:**

-   Completa el `break` cuando se acierta
-   Si ha acertado, muestra en cuántos intentos. Ojo: para _concatenar_ un número con texto, primero hay que convertirlo con `str()`
-   Si no ha acertado, sustituye el `...` por un mensaje que revele el número secreto

**Diagnóstico:** juega dos partidas: una en la que aciertes y otra en la que falles **a propósito** los seis intentos. Tienen que salir mensajes distintos. Si al fallar no aparece nada, revisa la condición del último `if`.

---


## Entrega {#entrega}

```text
PRACTICA1.2/
+-- adivina_el_numero.py   <-- el juego completo (¡sin el print del número secreto!)
+-- explicacion.md         <-- tus respuestas a "Explica tu código"
```

Súbela al **servidor SFTP del aula**:

```text
$ sftp tu_usuario@servidor-del-aula
sftp> put -r PRACTICA1.2
sftp> bye
```

Requisitos funcionales:

-   [ ] El número secreto cambia en cada partida
-   [ ] Se puede intentar un máximo de 6 veces
-   [ ] Después de cada intento, el juego dice "muy alta" o "muy baja"
-   [ ] Si se acierta, el bucle termina y se muestra el número de intentos
-   [ ] Si no se acierta, se revela el número secreto
-   [ ] Nombres en `snake_case` y comentarios en las partes clave

---


## Explica tu código {#explica-tu-código}

En `explicacion.md` responde con tus palabras:

1.  ¿Qué pasa si quitas la línea `estimacion = int(estimacion)`? Pruébalo y cuenta qué error sale y por qué
2.  ¿Qué diferencia hay entre `intentos_realizados = 0` e `intentos_realizados == 0`?
3.  ¿Qué hace `break`? ¿Qué pasaría si no estuviera?

---


## Rúbrica por competencias {#rúbrica-por-competencias}

| **Criterio**                    | **Hechicería (9-10)**                              | **Aprendizaje (6-8)**                              | **Iniciación (0-5)**           | **Peso** |
|---------------------------------|----------------------------------------------------|----------------------------------------------------|--------------------------------|----------|
| **Azar (`import` + `randint`)** | Número aleatorio correcto en cada partida          | Funciona pero el rango no es 1-20                  | Número fijo o sin `import`     | **15%**  |
| **Bucle `while` y bloques**     | 6 intentos exactos, sangría impecable              | El bucle funciona pero el número de intentos falla | Sin bucle o errores de sangría | **25%**  |
| **Conversión de tipos**         | `int()` y `str()` donde tocan; lo explica          | Convierte pero sin entender por qué                | `TypeError` al ejecutar        | **20%**  |
| **Condiciones, `if` y `break`** | Alta, baja y acierto correctos; `break` al acertar | Algún caso no se detecta bien                      | Las comparaciones no funcionan | **20%**  |
| **Experiencia de juego**        | Mensajes claros, veredicto final en los dos casos  | Falta el mensaje de derrota o es confuso           | No hay veredicto final         | **10%**  |
| **Explica tu código**           | Respuestas claras, con pruebas propias             | Respuestas correctas pero sin probar               | Sin `explicacion.md`           | **10%**  |

---


## Bonus (hasta +2.5) {#bonus--hasta-plus-2-dot-5}

| **Bonus**                     | **Descripción**                                                                    | **Puntos** |
|-------------------------------|------------------------------------------------------------------------------------|------------|
| Intervalo programable         | La jugadora elige el rango (1-50, 1-100...) antes de empezar                       | **+0.5**   |
| Intentos según dificultad     | Fácil, normal o difícil cambian el número de intentos                              | **+0.5**   |
| Entrada a prueba de despistes | Si escriben letras en vez de un número, el juego no se rompe (pista: `.isdigit()`) | **+0.5**   |
| Adivina la letra              | Versión alternativa: la esfera piensa una letra del alfabeto en vez de un número   | **+1.0**   |

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                  | **Dónde lo ves**                                                    |
|-------------------------------|---------------------------------------------------------------------|
| **Sentencia `import`**        | `import random` trae un módulo a tu programa                        |
| **`random.randint()`**        | Número entero al azar entre dos valores, ambos incluidos            |
| **Bucle `while`**             | Repite mientras `intentos_realizados < 6` sea `True`                |
| **Bloque**                    | Las líneas con la misma sangría debajo de un `while` o un `if`      |
| **Booleano**                  | `True` / `False`: el resultado de toda comparación                  |
| **Operadores de comparación** | `< > <= >= == !=`                                                   |
| **`=` frente a `==`**         | `=` guarda, `==` pregunta                                           |
| **Conversión de tipos**       | `int(estimacion)`, `str(intentos_realizados)`                       |
| **Sentencia `if`**            | Ejecuta un bloque solo si la condición se cumple                    |
| **`break`**                   | Sale del bucle antes de que la condición sea falsa                  |
| **Control de flujo**          | El orden en que se ejecutan las líneas cambia según las condiciones |

---

> _"La esfera no adivina nada: solo sabe comparar. Y ahora tú también."_
