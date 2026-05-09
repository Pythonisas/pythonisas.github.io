+++
title = "POO — Naves espaciales, coches y Python"
author = ["Jordi"]
date = 2026-03-15T12:00:00+01:00
publishDate = 2026-03-15
tags = ["prácticas"]
url = "/poo2/"
draft = false
+++

## Tabla de Contenido {#tabla-de-contenido}

1.  [Trabajando con Clases e Instancias — Naves Espaciales](#trabajando-con-clases-e-instancias-naves-espaciales)
2.  [La Clase Coche](#la-clase-coche)
3.  [Establecer un Valor por Defecto](#establecer-un-valor-por-defecto-para-un-atributo-de-nuestro-coche)
4.  [Modificando los Valores de Atributos](#modificando-los-valores-de-atributos-de-nuestro-coche)
5.


## Trabajando con Clases e Instancias — Naves Espaciales {#trabajando-con-clases-e-instancias-naves-espaciales}

¿Por que naves? Porque mas adelante (Capitulo 12) crearemos nuestro
propio videojuego **Alien Invasion** con Pygame, donde la clase `Ship`
sera el corazon del juego. Esta practica es el calentamiento.

> **Adelanto:** En `alien_invasion` la nave tendra atributos como
> `posicion_x`, `velocidad`, `moviendo_derecha` y metodos como
> `actualiza()` y `blitme()`. Hoy construimos la version "sin graficos"
> para dominar la mecanica de clases antes de llegar a Pygame.

Pero no corramos tanto! ... como diria el poeta, 'hagamos camino al andar'. Paso a paso.
Veamos un ejemplo de todo esto basado en unos vehiculos mas terrenales. Veamos un ejemplo basado en
coches y como manejar parametros como fabricante, año de fabricacion, kilometraje etc...


## La Clase `Coche` {#la-clase-coche}

Vamos a escribir una clase que represente un coche. Nuestra clase
almacenara informacion sobre el tipo de coche y tendra un metodo que
resuma esa informacion.


### Definicion basica de la clase {#definicion-basica-de-la-clase}

En la clase `Coche` definimos el metodo `__init__()` con el parametro
`self` en primer lugar, igual que hicimos con la clase `Pyrro` en la practica anterior.
Le damos tambien tres parametros mas: `fabricante`, `modelo` y `año`.

El metodo `__init__()` recibe estos parametros y los asigna a los
**atributos** que se asociaran con las instancias generadas a partir de
esta clase.

```python
class Coche:
    """Intento sencillo de representar un coche."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año

    def nombra_descriptivamente(self):
        """Devuelve un nombre descriptivo con formato legible."""
        nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_descriptivo.title()

mi_nuevo_coche = Coche('audi', 'a4', 2024)
print(mi_nuevo_coche.nombra_descriptivamente())
```

```text
2024 Audi A4
```


#### Que ocurre aqui {#que-ocurre-aqui}

-   `nombra_descriptivamente()` combina el año, la marca y el modelo en un solo string que describe el coche de forma legible.
-   Para acceder a los valores de los atributos dentro del metodo usamos `self.fabricante`, `self.modelo` y `self.año`.
-   Fuera de la clase, creamos una instancia de `Coche` y la asignamos a la variable `mi_nuevo_coche`.
-   Llamamos a `nombra_descriptivamente()` para mostrar que coche tenemos.


## Establecer un Valor por Defecto para un Atributo de 'nuestro coche' {#establecer-un-valor-por-defecto-para-un-atributo-de-nuestro-coche}

Cuando se crea una instancia, los atributos pueden definirse **sin
necesidad de pasarlos como parametros**. Estos atributos se definen
dentro del metodo `__init__()`, donde se les asigna un valor por
defecto.

Vamos a añadir un atributo llamado `lectura_cuentakilometros` que siempre
empiece con valor `0`. Tambien añadiremos un metodo `lee_cuentakilometros()`
que nos ayude a leer el cuentakilometros de cada coche.

```python
class Coche:
    """Intento sencillo de representar un coche."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.cuentakilomentros_lectura = 0           # valor por defecto

    def nombra_descriptivamente(self):
        """Devuelve un nombre descriptivo con formato legible."""
        nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_descriptivo.title()

    def lee_cuentakilometros(self):
        """Imprime el kilometraje del coche."""
        print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilometros.")

mi_nuevo_coche = Coche('audi', 'a4', 2024)
print(mi_nuevo_coche.nombra_descriptivamente())
mi_nuevo_coche.lee_cuentakilometros()
```

```text
2024 Audi A4
Este coche ha recorrido 0 kilometros.
```


#### Que ocurre aqui {#que-ocurre-aqui}

-   Python crea un nuevo atributo `cuentakilomentros_lectura` y le asigna el valor inicial `0` — no hace falta pasarlo como argumento al crear la instancia.
-   El metodo `lee_cuentakilometros()` simplemente imprime el valor actual del cuentakilometros.
-   Nuestro coche empieza con 0 millas. Pocos coches se venden con exactamente 0 millas, asi que necesitamos una forma de cambiar este valor...


## Modificando los Valores de Atributos de 'nuestro coche' {#modificando-los-valores-de-atributos-de-nuestro-coche}

Se puede cambiar el valor de un atributo de **tres formas**:

1.  Directamente a traves de la instancia
2.  A traves de un metodo (setter)
3.  Incrementandolo a traves de un metodo

Veamos cada enfoque.


### Forma 1 — Modificar un atributo directamente {#forma-1-modificar-un-atributo-directamente}

La forma mas sencilla es acceder al atributo directamente a traves de
la instancia usando la **notacion de punto**:

```python
class Coche:
    """Intento sencillo de representar un coche."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.cuentakilomentros_lectura = 0

    def nombra_descriptivamente(self):
        """Devuelve un nombre descriptivo con formato legible."""
        nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_descriptivo.title()

    def lee_cuentakilometros(self):
        """Imprime el kilometraje del coche."""
        print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilometros.")

mi_nuevo_coche = Coche('audi', 'a4', 2024)
print(mi_nuevo_coche.nombra_descriptivamente())

mi_nuevo_coche.cuentakilomentros_lectura = 23            # acceso directo
mi_nuevo_coche.lee_cuentakilometros()
```

```text
2024 Audi A4
Este coche ha recorrido 23 kilometros.
```

Esta linea le dice a Python: _toma la instancia `mi_nuevo_coche`, busca el
atributo `cuentakilometros_lectura` y asignale el valor 23_.

A veces querras acceder a los atributos directamente asi, pero otras
veces preferiras escribir un **metodo** que actualice el valor por ti.


### Forma 2 — Modificar un atributo mediante un metodo {#forma-2-modificar-un-atributo-mediante-un-metodo}

Es util tener metodos que actualicen ciertos atributos. En lugar de
acceder directamente, pasas el nuevo valor a un metodo que se encarga
de la actualizacion internamente.

```python
class Coche:
    """Intento sencillo de representar un coche."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.cuentakilomentros_lectura = 0

    def nombra_descriptivamente(self):
        """Devuelve un nombre descriptivo con formato legible."""
        nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_descriptivo.title()

    def lee_cuentakilometros(self):
        """Imprime el kilometraje del coche."""
        print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilometros.")

    def actualiza_cuentakilomentros(self, kilometraje):
        """Establece la lectura del cuentakilometros al valor dado."""
        self.cuentakilomentros_lectura = kilometraje

mi_nuevo_coche = Coche('audi', 'a4', 2024)
print(mi_nuevo_coche.nombra_descriptivamente())

mi_nuevo_coche.actualiza_cuentakilomentros(23)              # a traves de metodo
mi_nuevo_coche.lee_cuentakilometros()
```

```text
2024 Audi A4
Este coche ha recorrido 23 kilometros.
```


#### Añadir logica de proteccion {#añadir-logica-de-proteccion}

Podemos extender `actualiza_cuentakilomentros()` para que nadie intente
_retroceder_ el cuentakilometros:

```python
class Coche:
    """Intento sencillo de representar un coche."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.cuentakilomentros_lectura = 0

    def nombra_descriptivamente(self):
        """Devuelve un nombre descriptivo con formato legible."""
        nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_descriptivo.title()

    def lee_cuentakilometros(self):
        """Imprime el kilometraje del coche."""
        print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilometros.")

    def actualiza_cuentakilomentros(self, kilometraje):
        """
        Establece la lectura del cuentakilometros al valor dado.
        Rechaza el cambio si intenta retroceder el cuentakilometros.
        """
        if kilometraje >= self.cuentakilomentros_lectura:
            self.cuentakilomentros_lectura = kilometraje
        else:
            print("¡No puedes retroceder el cuentakilometros!")

mi_nuevo_coche = Coche('audi', 'a4', 2024)
mi_nuevo_coche.actualiza_cuentakilomentros(23)
mi_nuevo_coche.lee_cuentakilometros()

# Intentamos retroceder el odometro:
mi_nuevo_coche.actualiza_cuentakilomentros(10)
```

```text
Este coche ha recorrido 23 kilometros.
¡No puedes retroceder el cuentakilometros!
```

Ahora `actualiza_cuentakilomentros()` comprueba que la nueva lectura tiene
sentido antes de modificar el atributo. Si el valor proporcionado es
**mayor o igual** que el kilometraje existente, se actualiza. Si es
**menor**, se muestra una advertencia.


### Forma 3 — Incrementar un atributo mediante un metodo {#forma-3-incrementar-un-atributo-mediante-un-metodo}

A veces querras **sumar** una cantidad al valor de un atributo, en lugar
de asignarle un valor completamente nuevo.

Ejemplo: compramos un coche usado y le hacemos 100 millas entre la
compra y el registro.

```python
class Coche:
    """Intento sencillo de representar un coche."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.cuentakilomentros_lectura = 0

    def nombra_descriptivamente(self):
        """Devuelve un nombre descriptivo con formato legible."""
        nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
        return nombre_descriptivo.title()

    def lee_cuentakilometros(self):
        """Imprime el kilometraje del coche."""
        print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilometros.")

    def actualiza_cuentakilomentros(self, kilometraje):
        """
        Establece la lectura del cuentakilometros al valor dado.
        Rechaza el cambio si intenta retroceder el cuentakilometros.
        """
        if kilometraje >= self.cuentakilomentros_lectura:
            self.cuentakilomentros_lectura = kilometraje
        else:
            print("¡No puedes hacer retroceder el cuentakilometros!")

    def incrementa_cuentakilomentros(self, miles):
        """Suma la cantidad dada a la lectura del cuentakilometros."""
        self.cuentakilomentros_lectura += miles

mi_coche_usado = Coche('opel', 'corsa', 2019)
print(mi_coche_usado.nombra_descriptivamente())

mi_coche_usado.actualiza_cuentakilomentros(23_500)
mi_coche_usado.lee_cuentakilometros()

mi_coche_usado.incrementa_cuentakilomentros(100)
mi_coche_usado.lee_cuentakilometros()
```

```text
2019 Opel Corsa
Este coche ha recorrido 23500 kilometros.
Este coche ha recorrido 23600 kilometros.
```


#### Que ocurre aqui {#que-ocurre-aqui}

-   `incrementa_cuentakilomentros()` recibe un numero de millas y **suma** ese valor a `self.cuentakilomentros_lectura`.
-   Primero creamos un coche usado (`mi_coche_usado`).
-   Le asignamos 23.500 millas con `actualiza_cuentakilomentros()`.
-   Luego llamamos a `incrementa_cuentakilomentros(100)` para añadir las 100 millas recorridas entre la compra y el registro.

> **NOTA:** Puedes usar metodos como estos para controlar como los
> usuarios de tu programa actualizan valores como el cuentakilometros,
> pero cualquier persona con acceso al programa puede asignar
> directamente cualquier valor accediendo al atributo. La seguridad
> efectiva requiere una atencion extrema al detalle, ademas de las
> comprobaciones basicas mostradas aqui.


## Resumen de Conceptos {#resumen-de-conceptos}

| **Concepto**               | **Descripcion**                          | **Ejemplo**                                   |
|----------------------------|------------------------------------------|-----------------------------------------------|
| **Atributo con parametro** | Se pasa al crear la instancia            | `self.fabricante = fabricante`                |
| **Atributo por defecto**   | Se define en `__init__()` sin parametro  | `self.cuentakilomentros_lectura = 0`          |
| **Acceso directo**         | Modificar atributo con notacion de punto | `coche.cuentakilomentros_lectura = 23`        |
| **Metodo setter**          | Metodo que asigna un nuevo valor         | `actualiza_cuentakilomentros(23)`             |
| **Metodo incremento**      | Metodo que suma al valor existente       | `incrementa_cuentakilomentros(100)`           |
| **Logica de proteccion**   | Validacion dentro del setter             | `if kilometraje >` self.cuentakilomentros...= |
