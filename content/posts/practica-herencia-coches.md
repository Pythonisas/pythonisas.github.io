+++
title = "Práctica 3.4 — Clases, herencia y coches"
author = ["Fénix"]
date = 2026-03-23T12:00:00+01:00
publishDate = 2026-03-23
tags = ["prácticas"]
url = "/poo4/"
draft = false
+++

## Tabla de Contenidos {#tabla-de-contenidos}

1.  [Herencia](#herencia)
2.  [El metodo __init__() en una Clase Hija](#el-metodo-init--en-una-clase-hija)
3.  [Definir Atributos y Metodos para la Clase Hija](#definir-atributos-y-metodos-para-la-clase-hija)
4.  [Instancias como Atributos](#instancias-como-atributos)
5.  [Añadir mas detalle a la clase Bateria](#añadir-mas-detalle-a-la-clase-bateria)
6.  [Resumen de Conceptos](/poo4/#resumen-de-conceptos)
7.  [Diagrama de la Jerarquia](#diagrama-de-la-jerarquia)
8.  [Progresion del codigo](#progresion-del-codigo-las-4-versiones)


## Herencia {#herencia}

Cuando escribes clases no siempre tienes que partir de cero. Si la
clase que estas escribiendo es una **version especializada** de otra
clase que ya has escrito, puedes usar **herencia**. Cuando una clase
_hereda_ de otra, adquiere automaticamente todos los atributos y
metodos de la clase original. La clase original se llama **clase padre**
(o _parent class_), y la nueva clase es la **clase hija** (o _child
class_).

La clase hija hereda cada atributo y metodo de su padre, pero tambien
es libre de **definir atributos y metodos nuevos** propios.

> **Continuidad:** En la Practica 3.3 construimos la clase `Coche` y la
> clase `NaveEspacial` para dominar la mecanica de clases, atributos y
> metodos. Ahora vamos a **reutilizar** la clase `Coche` como padre para
> crear un tipo mas especifico: el **coche electrico**.


## El metodo `__init__()` en una Clase Hija {#el-metodo-init--en-una-clase-hija}

Cuando escribes una clase hija, lo primero que Python necesita hacer
es **inicializar los atributos de la clase padre**. Para ello, el
metodo `__init__()` de la clase hija llama al `__init__()` del padre.

Vamos a modelar un coche electrico. Un `CocheElectrico` es una
version especializada de `Coche`, asi que podemos basar `CocheElectrico`
en la clase `Coche` que ya tenemos y centrar nuestra codificacion
solamente en los atributos y comportamientos especificos de los
coches electricos.


### Version 0 — La herencia mas basica {#version-0-la-herencia-mas-basica}

Empecemos creando una version sencilla de `CocheElectrico` que haga
todo lo que puede hacer `Coche`:

```python
class Coche:
    """Intento sencillo de representar un coche."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.cuentakilometros_lectura = 0

    def nombra_descriptivamente(self):
        """Devuelve un nombre descriptivo con formato legible."""
        nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_descriptivo.title()

    def lee_cuentakilometros(self):
        """Imprime el kilometraje del coche."""
        print(f"Este coche ha recorrido {self.cuentakilometros_lectura} kilometros.")

    def update_cuentakilometros(self, kilometraje):
        """Establece la lectura del cuentakilometros al valor dado."""
        if kilometraje >= self.cuentakilometros_lectura:
            self.cuentakilometros_lectura = kilometraje
        else:
            print("¡No puedes retroceder el cuentakilometros!")

    def incrementa_cuentakilometros(self, kms):
        """Suma la cantidad dada a la lectura del cuentakilometros."""
        self.cuentakilometros_lectura += kms


class CocheElectrico(Coche):
    """Representa aspectos de un coche especificos de vehiculos electricos."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos de la clase padre."""
        super().__init__(fabricante, modelo, año)


mi_leaf = CocheElectrico('nissan', 'leaf', 2024)
print(mi_leaf.nombra_descriptivamente())
```

```text
2024 Nissan Leaf
```


#### Que ocurre aqui {#que-ocurre-aqui}

-   Empezamos con `Coche`. Cuando creas una clase hija, la clase padre debe estar definida **antes** en el mismo archivo. Aqui situamos `Coche` primero.
-   Definimos la clase hija: `CocheElectrico`. El nombre de la clase padre debe ir **entre parentesis** en la definicion de la clase hija: `class CocheElectrico(Coche):`
-   La funcion `super()` es una funcion especial que permite **llamar a un metodo de la clase padre**. La linea `super().__init__(fabricante, modelo, año)` le dice a Python que llame al `__init__()` de `Coche`, lo que da a `CocheElectrico` todos los atributos definidos en el padre. El nombre `super` viene de la convencion de llamar a la clase padre _superclase_ y a la hija _subclase_.
-   Probamos que la herencia funciona creando un coche electrico con los argumentos `'nissan'`, `'leaf'` y `2024`. Llamamos a `nombra_descriptivamente()`, que esta definida en `Coche` pero esta disponible en cualquier instancia de `CocheElectrico`.

> **En resumen:** aparte de `__init__()`, todavia no hay atributos ni metodos propios de un coche electrico. De momento, solo estamos comprobando que la herencia funciona correctamente.


## Definir Atributos y Metodos para la Clase Hija {#definir-atributos-y-metodos-para-la-clase-hija}

Una vez que tienes una clase hija que hereda de la padre, puedes
añadir cualquier **atributo y metodo nuevo** que sea necesario para
diferenciar la clase hija de la padre.

Vamos a añadir un atributo especifico de los coches electricos (el
tamaño de la bateria) y un metodo para informar sobre el.


### Version 1 — Atributos y metodos propios de la clase hija {#version-1-atributos-y-metodos-propios-de-la-clase-hija}

```python
class Coche:
    """Intento sencillo de representar un coche."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.cuentakilometros_lectura = 0

    def nombra_descriptivamente(self):
        """Devuelve un nombre descriptivo con formato legible."""
        nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_descriptivo.title()

    def lee_cuentakilometros(self):
        """Imprime el kilometraje del coche."""
        print(f"Este coche ha recorrido {self.cuentakilometros_lectura} kilometros.")

    def update_cuentakilometros(self, kilometraje):
        """Establece la lectura del cuentakilometros al valor dado."""
        if kilometraje >= self.cuentakilometros_lectura:
            self.cuentakilometros_lectura = kilometraje
        else:
            print("¡No puedes retroceder el cuentakilometros!")

    def incrementa_cuentakilometros(self, kms):
        """Suma la cantidad dada a la lectura del cuentakilometros."""
        self.cuentakilometros_lectura += kms


class CocheElectrico(Coche):
    """Representa aspectos de un coche especificos de vehiculos electricos."""

    def __init__(self, fabricante, modelo, año):
        """
        Inicializa los atributos de la clase padre.
        Despues inicializa los atributos especificos del coche electrico.
        """
        super().__init__(fabricante, modelo, año)
        self.tamaño_bateria = 40

    def describir_bateria(self):
        """Imprime una descripcion del tamaño de la bateria."""
        print(f"Este coche tiene una bateria de {self.tamaño_bateria} kWh.")


mi_leaf = CocheElectrico('nissan', 'leaf', 2024)
print(mi_leaf.nombra_descriptivamente())
mi_leaf.describir_bateria()
```

```text
2024 Nissan Leaf
Este coche tiene una bateria de 40 kWh.
```


#### Que ocurre aqui {#que-ocurre-aqui}

-   Añadimos el atributo `self.tamaño_bateria` y le asignamos un valor inicial de `40` (kWh). Este atributo se asociara a todas las instancias creadas a partir de `CocheElectrico` pero **no** a las instancias de `Coche`.
-   Tambien añadimos el metodo `describir_bateria()`, que imprime informacion sobre la bateria. Este metodo solo estara disponible para instancias de `CocheElectrico`.
-   No hay limite en cuanto puedes especializar la clase hija. Puedes añadir tantos atributos y metodos como necesites para modelar un coche electrico con la precision que quieras.

> **Consejo de diseño:** Si un atributo o metodo pertenece a _cualquier_ coche, no solo a un coche electrico, deberia ir en `Coche` y no en `CocheElectrico`. Cualquiera que use la clase `Coche` obtendra esa funcionalidad, y la clase `CocheElectrico` solo contendra lo especifico de los vehiculos electricos.


## Instancias como Atributos {#instancias-como-atributos}

Al modelar objetos del mundo real en codigo, puedes encontrar que
estas añadiendo mas y mas detalle a una clase. Llega un momento en
que tus listas de atributos y metodos crecen tanto que es buena idea
**extraer parte de la clase en una clase separada**. Puedes dividir tu
clase grande en clases mas pequeñas que trabajen juntas; esta tecnica
se llama **composicion**.

Por ejemplo, si seguimos añadiendo detalles a la clase
`CocheElectrico`, podriamos acabar con muchos atributos y metodos
especificos de la bateria. Cuando eso ocurre, podemos parar y mover
esos atributos y metodos a una clase separada llamada `Bateria`.
Entonces usamos una instancia de `Bateria` como **atributo** de
`CocheElectrico`:


### Version 2 — Instancias como atributos (composicion) {#version-2-instancias-como-atributos--composicion}

```python
class Coche:
    """Intento sencillo de representar un coche."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.cuentakilometros_lectura = 0

    def nombra_descriptivamente(self):
        """Devuelve un nombre descriptivo con formato legible."""
        nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_descriptivo.title()

    def lee_cuentakilometros(self):
        """Imprime el kilometraje del coche."""
        print(f"Este coche ha recorrido {self.cuentakilometros_lectura} kilometros.")

    def update_cuentakilometros(self, kilometraje):
        """Establece la lectura del cuentakilometros al valor dado."""
        if kilometraje >= self.cuentakilometros_lectura:
            self.cuentakilometros_lectura = kilometraje
        else:
            print("¡No puedes retroceder el cuentakilometros!")

    def incrementa_cuentakilometros(self, kms):
        """Suma la cantidad dada a la lectura del cuentakilometros."""
        self.cuentakilometros_lectura += kms


class Bateria:
    """Intento sencillo de modelar la bateria de un coche electrico."""

    def __init__(self, tamaño_bateria=40):
        """Inicializa los atributos de la bateria."""
        self.tamaño_bateria = tamaño_bateria

    def describir_bateria(self):
        """Imprime una descripcion del tamaño de la bateria."""
        print(f"Este coche tiene una bateria de {self.tamaño_bateria} kWh.")


class CocheElectrico(Coche):
    """Representa aspectos de un coche especificos de vehiculos electricos."""

    def __init__(self, fabricante, modelo, año):
        """
        Inicializa los atributos de la clase padre.
        Despues inicializa los atributos especificos del coche electrico.
        """
        super().__init__(fabricante, modelo, año)
        self.bateria = Bateria()


mi_leaf = CocheElectrico('nissan', 'leaf', 2024)
print(mi_leaf.nombra_descriptivamente())
mi_leaf.bateria.describir_bateria()
```

```text
2024 Nissan Leaf
Este coche tiene una bateria de 40 kWh.
```


#### Que ocurre aqui {#que-ocurre-aqui}

-   Definimos una nueva clase llamada `Bateria` que **no hereda de ninguna otra clase**. Su `__init__()` tiene un parametro `tamaño_bateria` con valor por defecto `40`. El metodo `describir_bateria()` tambien se ha movido aqui, desde `CocheElectrico`.
-   En `CocheElectrico`, ahora añadimos un atributo `self.bateria`. Esta linea le dice a Python que cree una nueva instancia de `Bateria` (con el valor por defecto de 40 kWh) y la asigne al atributo `self.bateria`. Esto ocurrira **cada vez que se llame a** `__init__()`; cualquier instancia de `CocheElectrico` tendra automaticamente una instancia de `Bateria` asociada.
-   Para acceder a los atributos de la bateria hay que usar **doble notacion de punto**: `mi_leaf.bateria.describir_bateria()`

> **¿Por que composicion?** Esto puede parecer mucho trabajo extra. Pero ahora puedes describir la bateria con todo el detalle que quieras **sin ensuciar** la clase `CocheElectrico`. Ademas, la clase `Bateria` es reutilizable: podria usarse en una moto electrica, un patinete, o cualquier otro vehiculo.


## Añadir mas detalle a la clase `Bateria` {#añadir-mas-detalle-a-la-clase-bateria}

Cuando la bateria es su propia clase, es natural seguir
enriqueciendola. Vas a añadir tu mismo/a un metodo `obtener_autonomia()` que
informe de la distancia que el coche puede recorrer segun el tamaño
de la bateria:


## Objetivo de la practica : ampliar las caracteristicas del coche {#objetivo-de-la-practica-ampliar-las-caracteristicas-del-coche}


### Inventa una Version 3 que implemente sobre la Version 2 un Metodo `obtener_autonomia()` {#inventa-una-version-3-que-implemente-sobre-la-version-2-un-metodo-obtener-autonomia}

> **Tu tarea:** Estudia cada version, ejecutala, modificala.
> Experimenta cambiando valores, añadiendo metodos, creando nuevas
> subclases. La mejor forma de aprender POO es _romper cosas y
> arreglarlas_.

<!--quoteend-->

> **Reflexion sobre el diseño:** En este punto podemos preguntarnos:
> ¿Donde deberia vivir un metodo como `obtener_autonomia()`? ¿En
> `CocheElectrico` o en `Bateria`? Si la autonomia depende **solo** del
> tamaño de la bateria, entonces pertenece a `Bateria`. Pero si la
> autonomia tambien dependiera del peso del coche, la aerodinamica, o
> el tipo de neumaticos... entonces quiza `CocheElectrico` seria mejor
> lugar. El arte de decidir donde poner cada metodo es lo que hace la
> POO interesante.

Demuestra tu arte como programador/a,

-   Ampliando unas 2 o 3 caracteristicas del vehiculo usando el concepto de **herencia**. Inspirate en como hemos hecho con la bateria.


## Resumen de Conceptos {#resumen-de-conceptos}

| **Concepto**                   | **Descripcion**                                     | **Ejemplo**                                 |
|--------------------------------|-----------------------------------------------------|---------------------------------------------|
| **Herencia**                   | Una clase hija adquiere atributos/metodos del padre | `class CocheElectrico(Coche):`              |
| **Clase padre (superclase)**   | La clase original de la que se hereda               | `Coche`                                     |
| **Clase hija (subclase)**      | La nueva clase que hereda y especializa             | `CocheElectrico`                            |
| **`super()`**                  | Llama a un metodo de la clase padre                 | `super().__init__(fabricante, modelo, año)` |
| **Atributo propio de la hija** | Atributo que solo existe en la subclase             | `self.tamaño_bateria = 40`                  |
| **Metodo propio de la hija**   | Metodo exclusivo de la subclase                     | `describir_bateria()`                       |
| **Composicion**                | Usar una instancia de otra clase como atributo      | `self.bateria = Bateria()`                  |
| **Doble notacion de punto**    | Acceder a atributos de un objeto anidado            | `mi_leaf.bateria.describir_bateria()`       |


## Diagrama de la Jerarquia {#diagrama-de-la-jerarquia}

```text
 ┌─────────────┐
 │   Coche     │  ← clase padre (superclase)
 │─────────────│
 │ fabricante  │
 │ modelo      │
 │ año         │
 │ cuentakm    │
 │─────────────│
 │ nombra..()  │
 │ lee_ckm()   │
 │ update_ckm()│
 │ increm_ckm()│
 └──────┬──────┘
        │ hereda
        ▼
┌───────────────┐
│CocheElectrico │  ← clase hija (subclase)
│───────────────│
│ bateria ──────┼──────┐
│───────────────│      │ composicion
│               │      ▼
└───────────────┘  ┌──────────┐
                   │ Bateria  │
                   │──────────│
                   │ tamaño   │
                   │──────────│
                   │ describir│
                   │ autonomia│
                   └──────────┘
```


## Progresion del codigo — las 4 versiones {#progresion-del-codigo-las-4-versiones}

A continuacion tienes un resumen de como hemos ido construyendo el
codigo, paso a paso:

| **Version** | **Fichero**              | **Que añade**                                        |
|-------------|--------------------------|------------------------------------------------------|
| **v0**      | `coche_electrico_v0.py`  | Herencia basica: `CocheElectrico(Coche)` + `super()` |
| **v1**      | `coche_electrico_v1.py`  | Atributo (`tamaño_bateria`) y metodo propios         |
| **v2**      | `coche_electrico_v2.py`  | Composicion: clase `Bateria` como atributo           |
|             | A Crear por Ti           | Caracteristicas adicionales del vehiculo.            |
| **v3**      | `coche_electrico_v3.py?` | Metodo `obtener_autonomia()` en `Bateria` ?          |

Happy coding !
