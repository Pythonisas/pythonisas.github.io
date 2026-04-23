+++
title = "Práctica 3.3 — Modelando Naves espaciales con Python"
author = ["Jordi"]
date = 2026-03-16T12:00:00+01:00
publishDate = 2026-03-16
tags = ["prácticas"]
url = "/poo3/"
draft = false
+++

{{< figure src="/images/nostromo.png" >}}


## Las Naves Espaciales como Clases Python {#las-naves-espaciales-como-clases-python}


## Descripcion {#descripcion}

Anteriormente modelamos un `Coche`. Vamos ahora a modelar una **nave espacial** usando Programacion Orientada a Objetos (POO).
La practica se compone de **dos scripts progresivos**:

| **Script**        | **Enfoque**                                  | **Concepto clave**                             |
|-------------------|----------------------------------------------|------------------------------------------------|
| `nave_basica.py`  | Clase sencilla con constructor y metodo      | **Clase, `__init__`, atributos, metodos**      |
| `nave_combate.py` | Clase completa con modificacion de atributos | **Setters, incrementos, logica de proteccion** |

> Primero construiras la nave con lo basico (`nave_basica.py`), y despues le daras escudos, combustible y la meteras en combate (`nave_combate.py`).

---


## Objetivo {#objetivo}

Completa los huecos marcados con `___` y `...` en los dos ficheros incompletos que se te proporcionan, de forma que:

1.  `nave_basica.py` — Define una clase `NaveEspacial` con atributos basicos y un metodo de descripcion
2.  `nave_combate.py` — Amplia la nave con escudo, combustible y metodos para recibir daño, consumir y recargar combustible

---


## Fichero 1: `nave_basica.py` (clase sencilla) {#fichero-1-nave-basica-dot-py--clase-sencilla}

Este script define una clase basica con constructor y un metodo. Completa los huecos:

```python
#!/usr/bin/env python3
# nave_basica.py — Mi primera nave espacial con POO

class ___:
    """Intento sencillo de representar una nave espacial."""

    def ___(self, nombre, tipo, velocidad_maxima):
        """Inicializa los atributos para describir una nave."""
        self.___ = nombre
        self.___ = tipo
        self.___ = velocidad_maxima

    def descripcion(___):
        """Devuelve una descripcion legible de la nave."""
        texto = f"{self.___} — {self.___} (max. {self.___} km/s)"
        return texto.title()


# --- Crear instancias y probarlas ---

mi_nave = ___(  'halcon milenario', 'carguero ligero', 1050)
nave_2  = ___('x-wing',            'caza estelar',    1050)

print(mi_nave.___())
print(nave_2.___())
```


### Pistas para `nave_basica.py` {#pistas-para-nave-basica-dot-py}

-   Una **clase** se define con `class NombreClase:` — el nombre de nuestra clase es `NaveEspacial`
-   El metodo **constructor** se llama `__init__` — se ejecuta automaticamente al crear cada objeto
-   `self` es la referencia al **propio objeto** — todos los metodos de instancia lo reciben como primer parametro
-   `self.atributo = valor` asigna un atributo al objeto dentro del constructor
-   Para **crear un objeto** (instancia), se llama a la clase como si fuera una funcion: `NombreClase(args...)`
-   Para llamar a un **metodo** del objeto, usa notacion de punto: `objeto.metodo()`

---


## Fichero 2: `nave_combate.py` (clase completa con combate) {#fichero-2-nave-combate-dot-py--clase-completa-con-combate}

Aqui ampliamos la nave con escudo, combustible y metodos de combate. Completa los huecos:

```python
#!/usr/bin/env python3
# nave_combate.py — Nave espacial con escudo, combustible y combate

class NaveEspacial:
    """Nave espacial con sistemas de escudo y combustible."""

    def __init__(self, nombre, tipo, velocidad_maxima):
        """Inicializa atributos basicos y valores por defecto."""
        self.nombre = nombre
        self.tipo = tipo
        self.velocidad_maxima = velocidad_maxima
        self.___ = 100        # escudo empieza al 100%
        self.___ = 100        # combustible empieza al 100%

    def descripcion(self):
        """Devuelve una descripcion legible de la nave."""
        texto = f"{self.nombre} — {self.tipo} (max. {self.velocidad_maxima} km/s)"
        return texto.title()

    def estado(self):
        """Imprime el estado actual de la nave."""
        print(f"Escudo: {self.___}% | Combustible: {self.___}%")


    # --- Forma 1: Modificar atributo directamente (se hace fuera de la clase) ---
    # (No hay metodo aqui — se accede con: mi_nave.nivel_escudo = 75)


    # --- Forma 2: Modificar atributo mediante un metodo (setter) ---

    def actualizar_escudo(self, nuevo_nivel):
        """
        Establece el nivel de escudo al valor dado.
        Limita el rango entre 0 y 100.
        """
        if nuevo_nivel ___ 0:
            self.nivel_escudo = 0
            print("¡Escudo desactivado! La nave es vulnerable.")
        elif nuevo_nivel ___ 100:
            self.nivel_escudo = 100
            print("El escudo no puede superar el 100%.")
        else:
            self.___ = nuevo_nivel


    # --- Forma 3: Incrementar/decrementar un atributo mediante un metodo ---

    def recibir_daño(self, puntos):
        """Reduce el escudo en la cantidad de puntos de daño recibidos."""
        self.nivel_escudo ___ puntos
        if self.nivel_escudo < 0:
            self.nivel_escudo = 0
        print(f"¡Impacto! Daño recibido: {puntos}. Escudo restante: {self.___}%")

    def consumir_combustible(___, cantidad):
        """Reduce el combustible en la cantidad consumida."""
        self.combustible ___ cantidad
        if ___.combustible < 0:
            self.combustible = 0
        print(f"Combustible consumido: {cantidad}. Restante: {self.combustible}%")

    def recargar(self, combustible_extra):
        """Suma combustible a la nave (sin superar el 100%)."""
        self.combustible ___ combustible_extra
        if self.combustible ___ 100:
            self.combustible = 100
        print(f"Recarga completada. Combustible: {self.___}%")


# --- Simulacion de mision ---

if __name__ == "___":

    mi_nave = ___('x-wing', 'caza estelar', 1050)
    print(mi_nave.___())
    mi_nave.___()

    print("\n--- Entramos en combate ---")
    mi_nave.___(30)
    mi_nave.___(45)

    print("\n--- Huimos a velocidad maxima ---")
    mi_nave.___(40)

    print("\n--- Llegamos a la base y recargamos ---")
    mi_nave.___(25)

    print("\n--- Estado final de la nave ---")
    mi_nave.___()
```


### Pistas para `nave_combate.py` {#pistas-para-nave-combate-dot-py}

-   Los atributos por defecto (`nivel_escudo`, `combustible`) se definen dentro de `__init__` **sin** pasarlos como parametro
-   En `actualizar_escudo()`: piensa que operador de comparacion necesitas — ¿"menor que" o "mayor que"?
-   `recibir_daño()` y `consumir_combustible()` **restan** del valor actual: el operador es `-=`
-   `recargar()` **suma** al valor actual: el operador es `+=`
-   `self` aparece como primer parametro en **todos** los metodos — ¡no lo olvides en `consumir_combustible`!
-   `__name__ =` "<span class="underline">_</span>"= — ¿Que valor especial tiene `__name__` cuando ejecutas un script directamente? (pista: empieza por doble guion bajo)
-   Para llamar a metodos: `objeto.nombre_del_metodo(argumentos)`

---


## Salida esperada {#salida-esperada}


### `nave_basica.py` {#nave-basica-dot-py}

```text
Halcon Milenario — Carguero Ligero (Max. 1050 Km/S)
X-Wing — Caza Estelar (Max. 1050 Km/S)
```


### `nave_combate.py` {#nave-combate-dot-py}

```text
X-Wing — Caza Estelar (Max. 1050 Km/S)
Escudo: 100% | Combustible: 100%

--- Entramos en combate ---
¡Impacto! Daño recibido: 30. Escudo restante: 70%
¡Impacto! Daño recibido: 45. Escudo restante: 25%

--- Huimos a velocidad maxima ---
Combustible consumido: 40. Restante: 60%

--- Llegamos a la base y recargamos ---
Recarga completada. Combustible: 85%

--- Estado final de la nave ---
Escudo: 25% | Combustible: 85%
```

---


## Entrega {#entrega}

-   Sube ambos ficheros (`nave_basica.py` y `nave_combate.py`) completados y funcionales
-   Asegurate de que ambos se ejecutan sin errores con `python3 nombre.py`
-   **No modifiques** los textos de los `print()` ni los docstrings — solo completa los huecos `___`

---


## BONUS — Amplia la nave (para nota maxima) {#bonus-amplia-la-nave--para-nota-maxima}

Si quieres ir a por el **10**, elige **una o mas** de estas ampliaciones:

| **Bonus**                    | **Descripcion**                                                                                                                       | **Puntos** |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------|
| Metodo `__str__()`           | Implementa `__str__` para que `print(mi_nave)` muestre la descripcion de la nave directamente                                         | +0.5       |
| Metodo `reparar_escudo(pts)` | Crea un metodo que sume puntos al escudo (sin superar 100%) — similar a `recargar()` pero para el escudo                              | +0.5       |
| Simulacion extendida         | Crea una segunda nave enemiga, hazlas combatir entre si (que una le haga `recibir_daño` a la otra) y muestra el estado final de ambas | +0.5       |

> Con el bonus puedes llegar hasta **10** puntos (maximo). No es necesario hacer todos.

---


## Conceptos clave que aprenderas {#conceptos-clave-que-aprenderas}

| **Concepto**                                                                              | **Donde lo ves**                                         |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------|
| **Clase y constructor `__init__`**                                                        | `class NaveEspacial:` → `def __init__(self, ...)`        |
| **Atributos de instancia**                                                                | `self.nombre`, `self.tipo`, `self.velocidad_maxima`      |
| **Atributos con valor por defecto**                                                       | `self.nivel_escudo = 100`, `self.combustible = 100`      |
| **Metodos de instancia**                                                                  | `descripcion()`, `estado()`, `recibir_daño()`, etc.      |
| **`self`**                                                                                | Primer parametro de todos los metodos                    |
| **Setter (Forma 2)**                                                                      | `actualizar_escudo(nuevo_nivel)` — asigna con validacion |
| **Incremento/Decremento (Forma 3)**                                                       | `+=` y `-=` dentro de metodos                            |
| **`if __name__ =` "<span class="underline"><span class="underline">main</span></span>"=** | Patron estandar para scripts ejecutables                 |

---

> _"Las naves de Star Wars y Alien no se programan solas... pero con POO, casi."_
