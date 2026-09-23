+++
title = "Práctica 1.1 — Academia Pythonisa I: Tus primeros hechizos"
author = ["Jordi"]
date = 2026-09-21T10:00:00+02:00
tags = ["prácticas"]
url = "/python1/"
draft = false
+++

{{< figure src="/images/pythonisa.png" >}}


## Misión: Despertar a la serpiente {#misión-despertar-a-la-serpiente}

**Contexto mágico:** Bienvenida, bienvenido a la **Academia de las Pythonisas**. Hasta hoy has escrito HTML y CSS: le _describías_ al navegador cómo tenía que verse una página. Aquí vas a aprender otra magia: **dar órdenes**. Tú escribes instrucciones, y la serpiente —el intérprete de Python— las ejecuta una tras otra, al pie de la letra.

Tu primera lección tiene tres partes: **hablar con la serpiente** (la consola interactiva), **guardar cosas en cajas** (las variables) y **escribir tu primer pergamino** (un programa `.py` que se puede guardar y volver a ejecutar).

> Basado en los Capítulos 1 y 2 de _Inventa tus propios juegos de computadora con Python_ -- Al Sweigart ([Cap. 1: La consola interactiva](https://github.com/JaquerEspeis/inventar-con-python/blob/master/capitulo1.md) · [Cap. 2: Escribiendo programas](https://github.com/JaquerEspeis/inventar-con-python/blob/master/capitulo2.md))

---


## Los problemas a resolver {#los-problemas-a-resolver}

1.  **Hablar con la consola** — ¿Cuánto da `2 + 3 * 4`? ¿Y `7 / 2` frente a `7 // 2`? La consola evalúa _expresiones_ (valores + operadores) y te devuelve un resultado. Tienes que aprender a **predecir** qué va a responder

2.  **Guardar valores** — Una variable es una caja con una etiqueta: guardas un valor y lo recuperas por su nombre. Pero si guardas algo nuevo en la misma caja, el valor anterior desaparece

3.  **Del eco al pergamino** — Lo que escribes en la consola se olvida al cerrarla. Para que tu magia perdure, la escribes en el **editor**, la guardas como fichero `.py` y la ejecutas cuantas veces quieras

4.  **Nombrar bien las cosas** — Python acepta casi cualquier nombre, pero la Academia tiene sus reglas (y el resto del mundo Python también: la guía de estilo **PEP 8**)

---


## Tu taller: la consola de Python {#tu-taller-la-consola-de-python}

En clase usaremos **Python 3.11**. Para empezar a programar más allá 1 o 2 líneas, más adelante, recomendaremos usar el sencillo **Sublime** como editor o [Thonny](https://thonny.org/) (o los clásicos editores _Nano_, _Emacs_... o _Vim_).

En esta primera práctica no necesitas nada de eso: te basta con **una terminal** y **un editor de texto cualquiera**.

| **Orden / tecla**    | **Para qué sirve**                                                 |
|----------------------|--------------------------------------------------------------------|
| `python3`            | Arranca la consola interactiva: aparece el símbolo `>>>`           |
| `>>>`                | Python espera una orden: la escribes, pulsas Enter y te responde   |
| Flecha ↑             | Recupera la última orden que escribiste (para no repetirla a mano) |
| `exit()` o `Ctrl+D`  | Sale de la consola y vuelve al terminal                            |
| `python3 fichero.py` | Ejecuta un programa que has guardado                               |

💡 ¿Qué versión de Python tienes? Escribe en la consola `import sys` y después `sys.version`.

---


## Herramientas a tu disposición {#herramientas-a-tu-disposición}

| **Herramienta**       | **Para qué sirve**                                             |
|-----------------------|----------------------------------------------------------------|
| `+ - * /`             | Sumar, restar, multiplicar, dividir (`/` siempre da decimales) |
| `//` y `%`            | División entera y resto                                        |
| `**`                  | Potencia: `2 ** 3` → `8`                                       |
| `( )`                 | Cambiar el orden de evaluación: `(2 + 3) * 4`                  |
| `variable = valor`    | Guardar un valor en una caja con nombre                        |
| `'texto'` o `"texto"` | Una cadena (_string_)                                          |
| `+` entre cadenas     | Concatenar: `'Hola' + 'Mundo'` → `'HolaMundo'` (¡sin espacio!) |
| `print(...)`          | Mostrar algo por pantalla                                      |
| `input()`             | Esperar a que la persona escriba algo y pulse Enter            |
| `#`                   | Comentario: Python ignora el resto de la línea                 |

---


## Desafío 1: La calculadora de la serpiente {#desafío-1-la-calculadora-de-la-serpiente}

Abre una terminal, escribe `python3` y trabaja en la **consola interactiva**. Para cada expresión, **primero apunta en papel lo que crees que dará**, y después compruébalo.

```text
>>> 2 + 2
>>> 2 + 3 * 4
>>> (2 + 3) * 4
>>> 8 * 3 / 2 + 2 + 7 - 9
>>> 7 / 2
>>> 7 // 2
>>> 7 % 2
>>> 2 ** 10
>>> 5 +
```

La última está mal **a propósito**. Lee el mensaje de error: ¿qué te está diciendo Python? ¿Dónde pone las marcas `^`?

**Diagnóstico:** si alguna predicción ha fallado, pregúntate **en qué orden** ha hecho Python las operaciones. Igual que en matemáticas: primero `**`, luego `* / // %`, y por último `+ -`.

---


## Desafío 2: Cajas mágicas {#desafío-2-cajas-mágicas}

Sigue en la Shell. Ahora vas a guardar valores en variables:

```text
>>> pociones = 15
>>> pociones
>>> pociones + 5
>>> pociones
>>> pociones = pociones + 5
>>> pociones
>>> pociones = 'ninguna'
>>> pociones
>>> hechizos + 1
```

Fíjate en tres cosas:

-   `pociones + 5` **calcula** un valor, pero no lo guarda. `pociones = pociones + 5` sí lo guarda
-   Una misma caja puede cambiar de número a texto: guardar un valor nuevo _borra_ el anterior
-   `hechizos` no existe: ¿qué error te da?

**Diagnóstico:** para mirar dentro de una caja en cualquier momento, escribe su nombre y pulsa Enter. La consola te responde con lo que guarda.

Copia **toda tu sesión de la consola** (desafíos 1 y 2) en un fichero `consola.txt`.

---


## Desafío 3: ¡Hola, Academia! {#desafío-3-hola-academia}

Ahora sí: tu primer programa. Sal de la consola (`exit()`), abre tu editor de texto, escribe esto y guárdalo como `hola_academia.py`. Después ejecútalo desde la terminal con `python3 hola_academia.py`:

```python
# Este programa saluda y pregunta por tu nombre.
print('¡Hola, Academia!')
print('¿Cómo te llamas?')
mi_nombre = input()
print('Es un placer conocerte, ' + mi_nombre)
```

Cuando funcione, **amplíalo**. El programa debe preguntar también:

-   el nombre de tu _familiar_ (tu mascota mágica: gato, cuervo, dragón de bolsillo...)
-   tu elemento favorito (fuego, agua, tierra, aire, bits...)

Y al final debe anunciar tu **nombre de Pythonisa**, uniendo todo con `+`. Por ejemplo:

```text
Desde hoy serás conocida como: Ada del Fuego, guardiana del cuervo Pixel
```

**Diagnóstico:** si te sale `Adadel Fuego` todo junto, recuerda que `+` pega las cadenas _tal cual_: los espacios tienes que ponerlos tú dentro de las comillas.

---


## Las reglas de los nombres {#las-reglas-de-los-nombres}

¿Te has fijado en que escribimos `mi_nombre` y no `miNombre` ni `mi_nómbre`? En la Academia seguimos la guía de estilo oficial de Python (PEP 8):

-   ✅ **snake_case**: minúsculas y palabras separadas por `_` → `mi_nombre`, `nombre_familiar`
-   ✅ **Sin tildes ni eñes** en los nombres de variables y de ficheros
-   ✅ Nombres que se entiendan → `elemento_favorito` mejor que `ef`

¿Por qué sin tildes, si Python 3 las admite? Por **portabilidad**. Tus programas viajarán entre Windows (en casa) y Linux (en el servidor del aula): un fichero llamado `adivinaElNúmero.py` puede aparecer como `adivinaElN├║mero.py` al copiarlo de un sistema a otro, y una variable con tilde es fácil de escribir mal en otro teclado. Los nombres simples, en minúscula y sin tildes funcionan igual en todas partes. _Los textos entre comillas sí pueden llevar todas las tildes que quieras._

---


## Entrega {#entrega}

```text
PRACTICA1.1/
+-- consola.txt          <-- sesión de la Shell (desafíos 1 y 2)
+-- hola_academia.py     <-- tu primer programa, ampliado
+-- explicacion.md       <-- tus respuestas a "Explica tu código"
```

Súbela al **servidor SFTP del aula** (usuario y servidor: los que te indique tu profe):

```text
$ sftp tu_usuario@servidor-del-aula
sftp> put -r PRACTICA1.1
sftp> ls
sftp> bye
```

También puedes usar FileZilla con el protocolo **SFTP**.

Requisitos funcionales:

-   [ ] `consola.txt` incluye todas las expresiones de los desafíos 1 y 2, incluidos los errores
-   [ ] `hola_academia.py` se ejecuta sin errores con `python3 hola_academia.py`
-   [ ] El programa pide al menos 3 datos con `input()` y compone el nombre de Pythonisa
-   [ ] Los nombres de variables siguen `snake_case`, sin tildes
-   [ ] El programa lleva al menos un comentario `#` explicando qué hace

---


## Explica tu código {#explica-tu-código}

En `explicacion.md` responde **con tus palabras** (no hace falta que sea largo):

1.  ¿Por qué `7 / 2` y `7 // 2` dan resultados distintos?
2.  En tu programa, ¿qué hay guardado en `mi_nombre` justo después de ejecutarse `input()`?
3.  ¿Qué pasa con el valor viejo de una variable cuando le guardas uno nuevo?

---


## Rúbrica por competencias {#rúbrica-por-competencias}

| **Criterio**                    | **Hechicería (9-10)**                                          | **Aprendizaje (6-8)**                                | **Iniciación (0-5)**                     | **Peso** |
|---------------------------------|----------------------------------------------------------------|------------------------------------------------------|------------------------------------------|----------|
| **Consola y expresiones**       | Todas las expresiones probadas, errores incluidos y comentados | Casi todas probadas, sin comentar los errores        | Faltan muchas o no hay `consola.txt`     | **25%**  |
| **Variables**                   | Guarda, recupera y sobrescribe valores; entiende la diferencia | Usa variables pero confunde calcular con guardar     | No usa variables                         | **20%**  |
| **Programa `hola_academia.py`** | Ampliado, 3+ `input()`, concatenación con espacios correctos   | Funciona pero sin ampliar o con espacios que faltan  | No ejecuta                               | **30%**  |
| **Nombres y estilo**            | `snake_case` sin tildes, nombres claros, comentarios útiles    | Nombres correctos pero poco claros o sin comentarios | camelCase, tildes o nombres de una letra | **15%**  |
| **Explica tu código**           | Respuestas claras, con sus palabras y ejemplos propios         | Respuestas correctas pero copiadas del enunciado     | Sin `explicacion.md` o respuestas vacías | **10%**  |

---


## Bonus (hasta +2) {#bonus--hasta-plus-2}

| **Bonus**                                 | **Descripción**                                                         | **Puntos** |
|-------------------------------------------|-------------------------------------------------------------------------|------------|
| Firma en arte ASCII                       | El programa termina mostrando tu nombre o un dibujo con caracteres      | **+0.5**   |
| Multiplicar cadenas                       | Descubre qué hace `'ja' * 3` y úsalo en tu programa                     | **+0.5**   |
| Cazadora de errores                       | Provoca a propósito un `TypeError` (`'5' + 5`) y explica por qué ocurre | **+0.5**   |
| Nombre aleatorio (pista: `import random`) | Investiga cómo elegir el elemento al azar                               | **+0.5**   |

---


## Conceptos clave {#conceptos-clave}

| **Concepto**          | **Dónde lo ves**                                                   |
|-----------------------|--------------------------------------------------------------------|
| **Expresión**         | `2 + 3 * 4`: valores y operadores que se evalúan a un único valor  |
| **Precedencia**       | `*` se calcula antes que `+`; los paréntesis mandan                |
| **Entero vs decimal** | `7 // 2` → `3` (`int`), `7 / 2` → `3.5` (`float`)                  |
| **Variable**          | `pociones = 15`: una caja con etiqueta                             |
| **Sobrescribir**      | `pociones = 'ninguna'` borra el `15` anterior                      |
| **Cadena (string)**   | `'¡Hola, Academia!'`: texto entre comillas                         |
| **Concatenación**     | `'Es un placer, ' + mi_nombre`                                     |
| **Llamada a función** | `print(...)`, `input()`: nombre + paréntesis                       |
| **Programa**          | Un fichero `.py` con instrucciones que se ejecutan de arriba abajo |

---

> _"Toda gran hechicera empezó escribiendo 2 + 2 y esperando, nerviosa, a que la serpiente respondiera 4."_
