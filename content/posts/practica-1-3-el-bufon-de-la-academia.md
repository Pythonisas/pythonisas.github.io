+++
title = "Práctica 1.3 — Academia Pythonisa III: El Bufón de la Academia"
author = ["Jordi"]
tags = ["prácticas"]
url = "/python3/"
draft = true
+++

## Misión: Hacer reír al tribunal {#misión-hacer-reír-al-tribunal}

**Contexto mágico:** Cada fin de trimestre, la Academia celebra el **Banquete de los Bits**, y este año te toca ser el Bufón o la Bufona. Tu programa tiene que contar chistes con buen ritmo: la pregunta, una pausa (¡el suspense!) y el remate. Parece fácil, pero enseguida te encontrarás con un enemigo inesperado: **las comillas**. ¿Cómo escribes un apóstrofo dentro de una cadena que ya empieza con comillas simples?

Esta práctica es corta y te servirá para dominar `print()`... y para aprender el **conjuro mejorado** que usaremos a partir de ahora: las **f-strings**.

> Basado en el Capítulo 4 de _Inventa tus propios juegos de computadora con Python_ -- Al Sweigart ([Cap. 4: Un programa que cuenta chistes](https://github.com/JaquerEspeis/inventar-con-python/blob/master/capitulo4.md))

---


## Los problemas a resolver {#los-problemas-a-resolver}

1.  **El ritmo** — Un chiste necesita una pausa antes del remate. ¿Cómo hace un programa para _esperar_ a que la persona pulse Enter?

2.  **Comillas dentro de comillas** — `'¿Por qué vuelan los pájaros pa'l sur?'` rompe el programa. ¿Por qué? ¿Cómo lo arreglas?

3.  **Caracteres invisibles** — Saltos de línea, tabuladores, la propia barra `\`... Hay caracteres que no se pueden escribir tal cual: necesitan un _código de escape_

4.  **Terminar la línea (o no)** — `print()` siempre salta de línea al acabar. A veces no quieres que lo haga

5.  **Concatenar cansa** — `'Hola, ' + nombre + ', tienes ' + str(edad) + ' años'` es largo y fácil de equivocar. Hay un hechizo mejor

---


## Herramientas a tu disposición {#herramientas-a-tu-disposición}

| **Herramienta**       | **Para qué sirve**                                                     |
|-----------------------|------------------------------------------------------------------------|
| `input()` sin guardar | Pausa hasta que se pulse Enter (no hace falta guardar lo que escriben) |
| `print()` vacío       | Imprime una línea en blanco                                            |
| `"..."` y `'...'`     | Si el texto lleva `'`, rodéalo de `"` (y al revés)                     |
| `\'` y `\"`           | Comilla escapada: se imprime la comilla, no cierra la cadena           |
| `\n`                  | Salto de línea                                                         |
| `\t`                  | Tabulador                                                              |
| `\\`                  | Una barra invertida de verdad                                          |
| `end=''`              | `print('Hola', end='')` no salta de línea al terminar                  |
| `f'...{variable}...'` | f-string: mete el valor de las variables directamente en el texto      |

---


## Desafío 1: Tu repertorio {#desafío-1-tu-repertorio}

Este es el esqueleto de un chiste, sacado del libro:

```python
print('¿Qué sale del cruce entre un mono y un pato?')
input()
print('¡Un monopatín!')
print()
```

**Requisitos:**

-   Crea `chistes.py` con **al menos 4 chistes tuyos** (o de tu familia, o de internet: ¡pero que sean para todos los públicos!)
-   Cada chiste tiene pregunta, pausa con `input()` y remate
-   Al menos uno debe tener _dos_ pausas (pregunta → "no sé, ¿qué?" → remate)

**Diagnóstico:** si el programa no para entre la pregunta y el remate, revisa que tienes el `input()` en medio.

---


## Desafío 2: La guerra de las comillas {#desafío-2-la-guerra-de-las-comillas}

**Requisitos:**

-   Al menos un chiste debe llevar un apóstrofo o unas comillas _dentro_ del texto. Resuélvelo de **las dos formas**: cambiando el tipo de comillas y usando `\'` o `\"`
-   Crea un **cartel del Banquete** con `\n` y `\t` en _un solo_ `print()`. Por ejemplo:

<!--listend-->

```text
=== BANQUETE DE LOS BITS ===
	Presenta:	La Bufona Ada
	Hora:		cuando compile
```

-   Usa `end=''` al menos una vez para que dos `print()` seguidos salgan en la misma línea

**Diagnóstico:** si Thonny te colorea medio programa del color de las cadenas, es que una comilla ha cerrado la cadena antes de tiempo. Busca la primera línea donde cambia el color.

💡 **Truco de bruja:** si pones una `r` delante de la cadena (`r'C:\nueva'`), Python **no** interpreta las barras: es una _cadena en bruto_. Te vendrá genial para el arte ASCII del Ahorcado.

---


## Desafío 3: El conjuro mejorado (f-strings) {#desafío-3-el-conjuro-mejorado--f-strings}

Haz que tu Bufón **pregunte el nombre** del público al principio y lo use en los chistes.

Primero hazlo **concatenando**, como hasta ahora:

```python
nombre = input('¿Cómo te llamas? ')
print('Oye, ' + nombre + ', ¿sabes cuál es el colmo de una programadora?')
```

Y después **reescríbelo con una f-string**:

```python
print(f'Oye, {nombre}, ¿sabes cuál es el colmo de una programadora?')
```

La `f` delante de las comillas le dice a Python: _todo lo que esté entre llaves `{ }` es una variable, sustitúyela por su valor_. Y además convierte los números a texto sola, sin `str()`:

```python
chistes_contados = 4
print(f'Hoy te he contado {chistes_contados} chistes, {nombre}.')
```

**Requisitos:**

-   El programa pide el nombre y lo usa al menos en 2 chistes
-   Al final muestra cuántos chistes ha contado, usando una f-string con un número
-   Deja **una** línea con concatenación comentada (con `#`) junto a su versión f-string, para comparar

**Diagnóstico:** si en pantalla sale literalmente `{nombre}`, te has olvidado la `f` delante de las comillas.

A partir de esta práctica, **usa f-strings** siempre que mezcles texto y variables.

---


## Entrega {#entrega}

```text
PRACTICA1.3/
+-- chistes.py        <-- tu repertorio completo
+-- explicacion.md    <-- tus respuestas a "Explica tu código"
```

Súbela al **servidor SFTP del aula** (`put -r PRACTICA1.3`).

Requisitos funcionales:

-   [ ] Al menos 4 chistes con pausa antes del remate
-   [ ] Comillas dentro de una cadena resueltas de las dos formas
-   [ ] Cartel con `\n` y `\t` en un solo `print()`
-   [ ] `end=''` usado al menos una vez
-   [ ] El nombre del público aparece en f-strings

---


## Explica tu código {#explica-tu-código}

1.  ¿Por qué `'pa'l sur'` da error y `"pa'l sur"` no?
2.  ¿Qué diferencia hay entre `print('a\nb')` y `print(r'a\nb')`? Pruébalo
3.  ¿Qué ventajas le ves a la f-string frente a la concatenación con `+`?

---


## Rúbrica por competencias {#rúbrica-por-competencias}

| **Criterio**             | **Hechicería (9-10)**                                          | **Aprendizaje (6-8)**                        | **Iniciación (0-5)**                 | **Peso** |
|--------------------------|----------------------------------------------------------------|----------------------------------------------|--------------------------------------|----------|
| **Ritmo y estructura**   | 4+ chistes, pausas bien colocadas, uno con doble pausa         | Chistes correctos pero sin doble pausa       | Menos de 3 chistes o sin pausas      | **20%**  |
| **Comillas y escapes**   | Resuelve las comillas de las dos formas; `\n`, `\t` correctos  | Solo una forma, o el cartel sale descuadrado | Errores de sintaxis por comillas     | **25%**  |
| **`end`**                | Lo usa con sentido (no solo por cumplir)                       | Lo usa pero sin efecto visible               | No aparece                           | **10%**  |
| **f-strings**            | Nombre y contador con f-strings; comparación con concatenación | f-strings correctas pero sin la comparación  | Sigue concatenando o sale `{nombre}` | **25%**  |
| **Estilo y creatividad** | Chistes propios, nombres claros, salida bien presentada        | Chistes del libro con pocos cambios          | Copia literal del libro              | **10%**  |
| **Explica tu código**    | Respuestas claras, con pruebas propias                         | Correctas pero sin probar                    | Sin `explicacion.md`                 | **10%**  |

---


## Bonus (hasta +1.5) {#bonus--hasta-plus-1-dot-5}

| **Bonus**            | **Descripción**                                                             | **Puntos** |
|----------------------|-----------------------------------------------------------------------------|------------|
| Arte ASCII del Bufón | Un gorro de bufón o una careta dibujada con caracteres (¿con `r'''...'''`?) | **+0.5**   |
| Suspense con puntos  | Los puntos suspensivos aparecen uno a uno (pista: `end=''` e `import time`) | **+0.5**   |
| Aplausómetro         | Tras cada chiste pregunta "¿te ha hecho gracia? (s/n)" y cuenta los "s"     | **+0.5**   |

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                   | **Dónde lo ves**                                                 |
|--------------------------------|------------------------------------------------------------------|
| **`input()` como pausa**       | No guardas el valor: solo esperas el Enter                       |
| **Comillas simples y dobles**  | `"pa'l sur"`: las de fuera no pueden aparecer dentro sin escapar |
| **Carácter de escape**         | `\n`, `\t`, `\'`, `\"`, `\\`                                     |
| **Cadena en bruto**            | `r'...'`: las barras `\` se quedan tal cual                      |
| **Argumento de palabra clave** | `end=''` cambia cómo termina `print()`                           |
| **f-string**                   | `f'Hola, {nombre}'`: variables dentro del texto                  |

---

> _"Un chiste sin pausa es como un programa sin `input()`: se acaba antes de empezar."_
