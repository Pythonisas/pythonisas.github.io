---
layout: page
title: "Práctica POO — Pyrro"
permalink: /poo/
---

![Pythonisa](/assets/img/pyrro-art-NLLM.png)

# 🐕 Práctica POO — Pyrro: Programación Orientada a Objetos con perros ASCII

## 📋 Descripción

Vamos a aprender **Programación Orientada a Objetos (POO)** en Python paso a paso, construyendo un programa que hace "hablar" a perros en arte ASCII.

La práctica se compone de **dos scripts progresivos**:

| **Script** | **Enfoque** | **Concepto clave** |
|:---|:---|:---|
| `pyrro-dice.py` | Funciones puras, sin clases | **Estilo funcional** |
| `pyrro-art.py` | Clase `Pyrro` con métodos y atributos | **POO (clases, objetos, métodos)** |

> 💡 Primero entenderás cómo funciona el script funcional (`pyrro-dice.py`), y después darás el salto a POO con `pyrro-art.py`.

---

## 🎯 Objetivo

Completa los huecos marcados con `___` y `...` en los dos ficheros incompletos que se te proporcionan, de forma que:

1. ✅ **`pyrro-dice.py`** — El perro "habla" mostrando un mensaje dentro de una viñeta ASCII
2. ✅ **`pyrro-art.py`** — Se define una clase `Pyrro` con atributos (`name`, `edad`, `raza`) y métodos que muestran arte ASCII según la raza

### 📥 Descarga los ficheros incompletos

- [pyrro-dice_incompleto.py](/assets/poo/pyrro-dice_incompleto.py)
- [pyrro-art_incompleto.py](/assets/poo/pyrro-art_incompleto.py)

Renómbralos a `pyrro-dice.py` y `pyrro-art.py` antes de empezar.

---

## 📄 Fichero 1: `pyrro-dice.py` (estilo funcional)

Este script usa **funciones puras** (sin clases). Completa los huecos:

```python
#!/usr/bin/env python3
# pyrro-dice.py — KISS + estilo funcional

import ___
import ___

PYRRO = r"""
        \  / \__
         \/  o  \
         /   (___)  GUAUU!
        /_____/
"""

def hacer_viñeta(___, width=40):
    lines = textwrap.wrap(___, width)
    max_len = max(len(l) for l in lines)
    border = "+" + "-" * (max_len + 2) + "+"
    body = "\n".join(f"| {l:<{max_len}} |" for l in lines)
    return f"{border}\n{body}\n{border}"

def pyrro_dice(___):
    print(hacer_viñeta(___))
    print(___)

if __name__ == "___":
    msg = " ".join(sys.argv[1:]) or "GUAU! Soy un buen perro."
    ___(msg)
```

### 🔍 Pistas para `pyrro-dice.py`

- 🐍 `textwrap` es un módulo de la biblioteca estándar que ayuda a formatear texto
- 🖥️ `sys` permite acceder a los argumentos de línea de comandos (`sys.argv`)
- 📝 `PYRRO` es una **constante** global que contiene el dibujo ASCII del perro
- 💬 `hacer_viñeta()` recibe un **texto** y devuelve una caja con bordes
- 🎯 `__name__ == "___"` — ¿Qué valor especial tiene `__name__` cuando ejecutas un script directamente?

---

## 📄 Fichero 2: `pyrro-art.py` (Programación Orientada a Objetos)

Aquí damos el salto a **POO**. Completa los huecos:

```python
#!/usr/bin/env python3
# pyrro-art.py — clase Pyrro con pyrro_dice() como método

import ___
import ___

# --- núcleo Funcional (reusable!) ---

def hacer_viñeta(text, width=40):
    lines = textwrap.wrap(text, width)
    max_len = max(len(l) for l in lines)
    border = "+" + "-" * (max_len + 2) + "+"
    body = "\n".join(f"| {l:<{max_len}} |" for l in lines)
    return f"{border}\n{body}\n{border}"

# --- Estilos de arte ASCII ---

PERROS = {
    "labrador": r"""
        \   / \__
         \ /  o  \
          /   (____)
         /___/  U
""",
    "___": r"""
        \   (  )
         \ (oo)
          /||\\
         (_||_)
          ^  ^
""",
    "___": r"""
        \  __  ____  __
         \/  \/    \/  \
         ( o            )--
          \____________/
""",
    "___": r"""
        \    / \
         \  (o o)
          \ / V \     guau. mucho perro.
           |  |  |    muy ascii.
           (__)__)
""",
}

# --- Clase Pyrro con pyrro_dice() como método ---

class ___:
    def __init__(self, name, edad, raza="labrador"):
        self.___ = name
        self.___ = edad
        self.___ = raza if raza in PERROS else "labrador"

    def sentarse(___):
        print(f"{self.name} ahora se sienta.")

    def dar_la_vuelta(self):
        print(f"{___.name} se da la vuelta!")

    def pyrro_dice(self, message=None):
        msg = message or f"Hola! Soy {self.___}, tengo {self.___} años. Guauu!"
        print(hacer_viñeta(___))
        print(PERROS[self.___])

    def arte_aleatorio(self, message=None):
        """Elige un arte de raza al azar."""
        self.raza = random.___(list(PERROS.___()))
        self.___(message)


# --- demo principal ---

if __name__ == "__main__":
    willie = ___("Willie", 6, "labrador")
    lucy   = ___("Lucy",   3, "shiba")
    rex    = ___("Rex",    5, "salchicha")

    willie.pyrro_dice("Creo que tengo pulgas. Guauauuu.")
    lucy.___(  "Me meo... donde lo hago, que no me vean?")
    rex.pyrro_dice("puedo ser alargado, pero mi código fuente no lo es.")

    print("--- Arte aleatorio ---")
    Pyrro("Buddy", 2).___(  "Raza sorpresa!")
```

### 🔍 Pistas para `pyrro-art.py`

- 🏗️ Una **clase** se define con `class NombreClase:` — ¿Cuál es el nombre de nuestra clase?
- 🐕 El método `__init__` es el **constructor**: se ejecuta al crear cada objeto. Asigna los atributos con `self.atributo = valor`
- 🔑 `self` es la referencia al **propio objeto** — todos los métodos de instancia lo reciben como primer parámetro
- 🎲 `random.choice()` elige un elemento al azar de una lista
- 📖 `.keys()` devuelve las claves de un diccionario
- 🐩 Las razas disponibles son: `labrador`, `caniche`, `salchicha`, `shiba`

---

## ✅ Salida esperada

### `pyrro-dice.py`

```bash
$ python3 pyrro-dice.py Hola mundo desde la terminal
+------------------------------------------+
| Hola mundo desde la terminal             |
+------------------------------------------+
        \  / \__
         \/  o  \
         /   (___)  GUAUU!
        /_____/
```

### `pyrro-art.py`

```bash
$ python3 pyrro-art.py
+------------------------------------------+
| Creo que tengo pulgas. Guauauuu.         |
+------------------------------------------+
        \   / \__
         \ /  o  \
          /   (____)
         /___/  U

+------------------------------------------+
| Me meo... donde lo hago, que no me vean? |
+------------------------------------------+
        \    / \
         \  (o o)
          \ / V \     guau. mucho perro.
           |  |  |    muy ascii.
           (__)__)

+------------------------------------------+
| puedo ser alargado, pero mi código       |
| fuente no lo es.                         |
+------------------------------------------+
        \  __  ____  __
         \/  \/    \/  \
         ( o            )--
          \____________/

--- Arte aleatorio ---
+------------------------------------------+
| Raza sorpresa!                           |
+------------------------------------------+
        [... arte ASCII aleatorio ...]
```

---

## 📦 Entrega

- Sube ambos ficheros (`pyrro-dice.py` y `pyrro-art.py`) completados y funcionales
- Asegúrate de que ambos se ejecutan sin errores con `python3 nombre.py`
- **No modifiques** el arte ASCII de los perros — solo completa los huecos `___`

---

## 🌟 BONUS — Amplía la clase (para nota máxima)

Si quieres ir a por el **10**, elige **una o más** de estas ampliaciones:

| **Bonus** | **Descripción** | **Puntos** |
|:---|:---|:---:|
| 🐕 **Nueva raza** | Añade una 5ª raza al diccionario `PERROS` con su arte ASCII propio | **+0.5** |
| 🎂 **Método `cumpleaños()`** | Crea un método que incremente `self.edad` en 1 y muestre un mensaje festivo | **+0.5** |
| 📊 **Método `__str__()`** | Implementa `__str__` para que `print(willie)` muestre info del perro | **+0.5** |

> 💡 Con el bonus puedes llegar hasta **10** puntos (máximo). No es necesario hacer todos.

---

## 🧠 Conceptos clave que aprenderás

| **Concepto** | **Dónde lo ves** |
|:---|:---|
| **Funciones puras** | `hacer_viñeta()` en ambos scripts |
| **Constantes globales** | `PYRRO` y `PERROS` (diccionario) |
| **Clase y constructor `__init__`** | `class Pyrro:` → `def __init__(self, ...)` |
| **Atributos de instancia** | `self.name`, `self.edad`, `self.raza` |
| **Métodos de instancia** | `sentarse()`, `pyrro_dice()`, `arte_aleatorio()` |
| **`self`** | Primer parámetro de todos los métodos |
| **Diccionarios** | `PERROS = { "labrador": ..., "caniche": ... }` |
| **`if __name__ == "__main__"`** | Patrón estándar para scripts ejecutables |

---

## 📊 Rúbrica de evaluación

### Fichero 1: `pyrro-dice.py` (Estilo funcional) — 3 puntos

| **Criterio** | **Puntos** | **Descripción** |
|:---|:---:|:---|
| **Imports correctos** | **0.5** | Importa `sys` y `textwrap` correctamente |
| **`hacer_viñeta()` completa** | **1** | El parámetro `text` está bien colocado y la función genera la viñeta correctamente |
| **`pyrro_dice()` completa** | **1** | Recibe `message`, llama a `hacer_viñeta()` e imprime `PYRRO` |
| **`__main__` correcto** | **0.5** | Usa `"__main__"` y llama a `pyrro_dice(msg)` |

### Fichero 2: `pyrro-art.py` (POO) — 6 puntos

| **Criterio** | **Puntos** | **Descripción** |
|:---|:---:|:---|
| **Imports correctos** | **0.5** | Importa `textwrap` y `random` |
| **Razas del diccionario** | **0.5** | Completa las claves: `caniche`, `salchicha`, `shiba` |
| **Definición de la clase** | **1** | `class Pyrro:` — nombre correcto de la clase |
| **Constructor `__init__`** | **1** | Asigna correctamente `self.name`, `self.edad`, `self.raza` |
| **Uso de `self`** | **1** | `self` como primer parámetro en `sentarse()` y referencia correcta en `dar_la_vuelta()` |
| **Método `pyrro_dice()`** | **1** | Accede a `self.name`, `self.edad`, pasa `msg` a `hacer_viñeta()`, usa `self.raza` como clave |
| **Método `arte_aleatorio()`** | **0.5** | Usa `random.choice()`, `.keys()` y llama a `self.pyrro_dice()` |
| **Bloque `__main__`** | **0.5** | Instancia objetos con `Pyrro(...)` y llama a los métodos correctos |

### Resumen

| **Parte** | **Puntos** |
|:---|:---:|
| `pyrro-dice.py` (funcional) | **3** |
| `pyrro-art.py` (POO) | **6** |
| **Total base** | **9** |
| BONUS (hasta +1.5) | **máx. 10** |

### Penalizaciones

| **Motivo** | **Penalización** |
|:---|:---:|
| El script no ejecuta (`SyntaxError`, `NameError`...) | **-1** por script |
| Arte ASCII modificado (se pidió no tocarlo) | **-0.5** |
| Copia literal de otro compañero | **0 puntos** (ambos) |

---

> 💬 *"En POO, los objetos son como los perros: cada uno tiene su nombre, su edad y su propia forma de ladrar."* 🐕
