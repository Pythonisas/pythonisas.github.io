+++
title = "Grimorio básico de Python"
author = ["Jordi"]
tags = ["recursos"]
url = "/grimorio/"
draft = true
+++

{{< figure src="/images/pythonisa.png" >}}


## Tu libro de hechizos de bolsillo {#tu-libro-de-hechizos-de-bolsillo}

Toda aprendiz de la Academia lleva encima un _grimorio_: una chuleta con los hechizos básicos que usará una y otra vez. Este es el tuyo. No hace falta memorizarlo: tenlo abierto en una pestaña mientras programas, y vuelve a él cada vez que dudes.

> Resumen de los capítulos 1 a 9 de _Inventa tus propios juegos de computadora con Python_ -- Al Sweigart ([traducción de JáquerEspeis](https://github.com/JaquerEspeis/inventar-con-python), CC BY-NC-SA)

---


## Tipos de datos {#tipos-de-datos}

| **Tipo** | **Qué guarda**        | **Ejemplos**                  | **Conversión** |
|----------|-----------------------|-------------------------------|----------------|
| `int`    | Números enteros       | `42`, `-7`, `0`               | `int('42')`    |
| `float`  | Números con decimales | `3.14`, `-0.5`, `2.0`         | `float('3.5')` |
| `str`    | Texto (cadenas)       | `'hola'`, `"Pythonisa"`, `''` | `str(7)`       |
| `bool`   | Verdadero o falso     | `True`, `False`               | `bool(0)`      |

⚠️ `input()` **siempre** devuelve un `str`. Si necesitas un número, conviértelo: `int(input())`.

---


## Operadores {#operadores}

| **Operador** | **Significado**          | **Ejemplo**           | **Resultado**    |
|--------------|--------------------------|-----------------------|------------------|
| `+`          | Suma / concatena         | `2 + 3`, `'ab' + 'c'` | `5`, `'abc'`     |
| `-`          | Resta                    | `10 - 4`              | `6`              |
| `*`          | Multiplica / repite      | `3 * 4`, `'ja' * 3`   | `12`, `'jajaja'` |
| `/`          | División (con decimales) | `7 / 2`               | `3.5`            |
| `//`         | División entera          | `7 // 2`              | `3`              |
| `%`          | Resto (módulo)           | `7 % 2`               | `1`              |
| `**`         | Potencia                 | `2 ** 10`             | `1024`           |

**Comparación** (devuelven `True` o `False`): `==` igual · `!=` distinto · `<` · `>` · `<=` · `>=`

**Booleanos:** `and` (las dos ciertas) · `or` (al menos una cierta) · `not` (lo contrario)

⚠️ `=` **guarda** un valor en una variable. `==` **pregunta** si dos valores son iguales.

---


## Estructuras de control {#estructuras-de-control}

```python
# Decidir
if intentos < 6:
    print('Sigue intentándolo')
elif intentos == 6:
    print('Último intento')
else:
    print('Se acabó')

# Repetir mientras se cumpla una condición
while respuesta != 'salir':
    respuesta = input()

# Repetir un número fijo de veces / recorrer una secuencia
for letra in 'python':
    print(letra)

for i in range(3):      # 0, 1, 2
    print(i)

# Salir de un bucle antes de tiempo
while True:
    if input() == 'fin':
        break
```

---


## Funciones {#funciones}

```python
def saludar(nombre):              # nombre es un PARÁMETRO
    mensaje = 'Hola, ' + nombre   # mensaje es LOCAL: solo existe aquí dentro
    return mensaje                # devuelve un valor a quien llamó

texto = saludar('Hipatia')        # 'Hipatia' es un ARGUMENTO
print(texto)
```

---


## Cadenas y listas {#cadenas-y-listas}

| **Hechizo**             | **Qué hace**                          | **Ejemplo → Resultado**               |
|-------------------------|---------------------------------------|---------------------------------------|
| `len(x)`                | Longitud                              | `len('dragón')` → `6`                 |
| `.lower()` / `.upper()` | Minúsculas / mayúsculas               | `'SÍ'.lower()` → `'sí'`               |
| `.split()`              | Parte una cadena en una lista         | `'a b c'.split()` → `['a', 'b', 'c']` |
| `x[i]`                  | Elemento en la posición `i` (desde 0) | `'gato'[0]` → `'g'`                   |
| `x[i:j]`                | Corte: de `i` hasta `j` (sin incluir) | `'pythonisa'[0:6]` → `'python'`       |
| `.append(x)`            | Añade al final de una lista           | `pociones.append('elixir')`           |
| `.reverse()`            | Da la vuelta a una lista              | `[1, 2, 3]` → `[3, 2, 1]`             |
| `x in y`                | ¿Está `x` dentro de `y`?              | `'a' in 'gato'` → `True`              |
| `f'...{var}...'`        | f-string: mete variables en el texto  | `f'Hola, {nombre}'`                   |

---


## Módulos que usaremos {#módulos-que-usaremos}

| **Módulo** | **Hechizo**             | **Para qué**                                         |
|------------|-------------------------|------------------------------------------------------|
| `random`   | `random.randint(1, 20)` | Número entero al azar entre 1 y 20 (ambos incluidos) |
| `random`   | `random.choice(lista)`  | Elemento al azar de una lista                        |
| `time`     | `time.sleep(2)`         | Pausa de 2 segundos (¡suspense!)                     |

---


## Nombres de variables: las reglas de la Academia {#nombres-de-variables-las-reglas-de-la-academia}

-   ✅ `snake_case`: palabras en minúscula separadas por `_` → `mi_nombre`, `intentos_realizados`
-   ✅ Sin tildes ni eñes en los nombres → `numero`, `anio`, no `número` ni `año`
-   ✅ Nombres que expliquen lo que guardan → `palabra_secreta` mejor que `p`
-   ✅ Constantes (valores que no cambian) en MAYÚSCULAS → `IMAGENES_AHORCADO`
-   ❌ No pueden empezar por número ni tener espacios o guiones → `2vidas`, `mi nombre`, `mi-nombre`

---


## Los errores más frecuentes {#los-errores-más-frecuentes}

| **Error**          | **Qué suele significar**                                                        |
|--------------------|---------------------------------------------------------------------------------|
| `SyntaxError`      | Has escrito algo que Python no entiende: falta `:`, un paréntesis o una comilla |
| `IndentationError` | La sangría (los espacios al principio de línea) no cuadra                       |
| `NameError`        | Usas una variable que no existe (¿mal escrita? ¿aún no creada?)                 |
| `TypeError`        | Mezclas tipos que no casan: `'5' + 5`                                           |
| `ValueError`       | El tipo es correcto pero el valor no: `int('hola')`                             |

💡 Python 3.11 marca con `^^^^` el punto exacto del error. **Lee el mensaje de abajo arriba**: la última línea te dice qué pasó, las de arriba dónde.
