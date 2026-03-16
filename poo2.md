---
layout: page
title: "POO — Naves espaciales, coches y Python"
permalink: /poo2/
---


# Tabla de Contenido

1.  [Trabajando con Clases e Instancias — Naves Espaciales](#org9fad1d0)
2.  [La Clase `Coche`](#org13c5b24)
    1.  [Definición básica de la clase](#orgfa01631)
3.  [Establecer un Valor por Defecto para un Atributo de 'nuestro coche'](#orgbe573ca)
4.  [Modificando los Valores de Atributos de 'nuestro coche'](#org0994e11)
    1.  [Forma 1 — Modificoche un atributo directamente](#org64136c1)
    2.  [Forma 2 — Modificoche un atributo mediante un método](#org9077a61)
    3.  [Forma 3 — Incrementar un atributo mediante un método](#org2041a3e)
5.  [Resumen de Conceptos](#orgff15180)



<a id="org9fad1d0"></a>

# Trabajando con Clases e Instancias — Naves Espaciales

En la práctica anterior modelamos un `Coche`. Ahora vamos a modelar
una **nave espacial** usando exactamente los mismos conceptos de OOP.

¿Por qué naves? Porque más adelante (Capítulo 12) crearemos nuestro
propio videojuego **Alien Invasion** con Pygame, donde la clase `Ship`
será el corazón del juego. Esta práctica es el calentamiento.

> **Adelanto:** En `alien_invasion` la nave tendrá atributos como
> `posicion_x`, `velocidad`, `moviendo_derecha` y métodos como
> `update()` y `blitme()`. Hoy construimos la versión "sin gráficos"
> para dominar la mecánica de clases antes de llegar a Pygame.

Pero no corramos tanto! &#x2026; como diría el poeta, 'hagamos camino al andar'. Paso a paso.
Veamos un ejemplo de todo esto basado en unos vehículos más terrenales. Veamos un ejemplo baso en
coches y como manejar parámetros como fabricante, año de fabricación, kilometraje etc&#x2026;


<a id="org13c5b24"></a>

# La Clase `Coche`

Vamos a escribir una clase que represente un coche. Nuestra clase
almacenará información sobre el tipo de coche y tendrá un método que
resuma esa información.


<a id="orgfa01631"></a>

## Definición básica de la clase

En la clase `Coche` definimos el método `__init__()` con el parámetro
`self` en primer lugar, igual que hicimos con la clase `Pyrro` en la práctica anterior.
Le damos también tres parámetros más: `fabricante`, `modelo` y `año`.

El método `__init__()` recibe estos parámetros y los asigna a los
**atributos** que se asociarán con las instancias generadas a partir de
esta clase.

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

    2024 Audi A4


### Qué ocurre aquí

-   `nombra_descriptivamente()` combina el año, la marca y el modelo en un
    solo string que describe el coche de forma legible.
-   Para acceder a los valores de los atributos dentro del método usamos
    `self.fabricante`, `self.modelo` y `self.año`.
-   Fuera de la clase, creamos una instancia de `Coche` y la asignamos a
    la variable `mi_nuevo_coche`.
-   Llamamos a `nombra_descriptivamente()` para mostrar qué coche tenemos.


<a id="orgbe573ca"></a>

# Establecer un Valor por Defecto para un Atributo de 'nuestro coche'

Cuando se crea una instancia, los atributos pueden definirse **sin
necesidad de pasarlos como parámetros**. Estos atributos se definen
dentro del método `__init__()`, donde se les asigna un valor por
defecto.

Vamos a añadir un atributo llamado `lectura_cuentakilometros` que siempre
empiece con valor `0`. También añadiremos un método `lee_cuentakilometros()`
que nos ayude a leer el cuentakilómetros de cada coche.

    class Coche:
    	"""Intento sencillo de representar un coche."""
    
    	def __init__(self, fabricante, modelo, año):
    		"""Inicializa los atributos para describir un coche."""
    		self.fabricante = fabricante
    		self.modelo = modelo
    		self.año = año
    		self.cuentakilomentros_lectura = 0           # ← valor por defecto
    
    	def nombra_descriptivamente(self):
    		"""Devuelve un nombre descriptivo con formato legible."""
    		nombre_descriptivo = f"{self.año} {self.fabricante} {self.modelo}"
    		return nombre_descriptivo.title()
    
    	def lee_cuentakilometros(self):
    		"""Imprime el kilometraje del coche."""
    		print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilómetros.")
    
    mi_nuevo_coche = Coche('audi', 'a4', 2024)
    print(mi_nuevo_coche.nombra_descriptivamente())
    mi_nuevo_coche.lee_cuentakilometros()

    2024 Audi A4
    Este coche ha recorrido 0 kilómetros.


### Qué ocurre aquí

-   Python crea un nuevo atributo `cuentakilomentros_lectura` y le asigna el
    valor inicial `0` — no hace falta pasarlo como argumento al crear
    la instancia.
-   El método `lee_cuentakilometros()` simplemente imprime el valor actual del
    cuentakilómetros.
-   Nuestro coche empieza con 0 millas. Pocos coches se venden con
    exactamente 0 millas, así que necesitamos una forma de cambiar este
    valor&#x2026;


<a id="org0994e11"></a>

# Modificando los Valores de Atributos de 'nuestro coche'

Se puede cambiar el valor de un atributo de **tres formas**:

1.  Directamente a través de la instancia
2.  A través de un método (setter)
3.  Incrementándolo a través de un método

Veamos cada enfoque.


<a id="org64136c1"></a>

## Forma 1 — Modifica del coche un atributo directamente

La forma más sencilla es acceder al atributo directamente a través de
la instancia usando la **notación de punto**:

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
    		print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilómetros.")
    
    mi_nuevo_coche = Coche('audi', 'a4', 2024)
    print(mi_nuevo_coche.nombra_descriptivamente())
    
    mi_nuevo_coche.cuentakilomentros_lectura = 23            # ← acceso directo
    mi_nuevo_coche.lee_cuentakilometros()

    2024 Audi A4
    Este coche ha recorrido 23 kilómetros.

Esta línea le dice a Python: *toma la instancia `mi_nuevo_coche`, busca el
atributo `cuentakilometros_lectura` y asígnale el valor 23*.

A veces querrás acceder a los atributos directamente así, pero otras
veces preferirás escribir un **método** que actualice el valor por ti.


<a id="org9077a61"></a>

## Forma 2 — Modifica del coche che un atributo mediante un método

Es útil tener métodos que actualicen ciertos atributos. En lugar de
acceder directamente, pasas el nuevo valor a un método que se encochega
de la actualización internamente.

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
    		print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilómetros.")
    
    	def update_cuentakilomentros(self, kilometraje):
    		"""Establece la lectura del cuentakilómetros al valor dado."""
    		self.cuentakilomentros_lectura = kilometraje
    
    mi_nuevo_coche = Coche('audi', 'a4', 2024)
    print(mi_nuevo_coche.nombra_descriptivamente())
    
    mi_nuevo_coche.update_cuentakilomentros(23)              # ← a través de método
    mi_nuevo_coche.lee_cuentakilometros()

    2024 Audi A4
    Este coche ha recorrido 23 kilómetros.


### Añadir lógica de protección

Podemos extender `update_cuentakilomentros()` para que nadie intente
*retroceder* el cuentakilómetros:

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
    		print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilómetros.")
    
    	def update_cuentakilomentros(self, kilometraje):
    		"""
    		Establece la lectura del cuentakilómetros al valor dado.
    		Rechaza el cambio si intenta retroceder el cuentakilómetros.
    		"""
    		if kilometraje >= self.cuentakilomentros_lectura:
    			self.cuentakilomentros_lectura = kilometraje
    		else:
    			print("¡No puedes retroceder el cuentakilómetros!")
    
    mi_nuevo_coche = Coche('audi', 'a4', 2024)
    mi_nuevo_coche.update_cuentakilomentros(23)
    mi_nuevo_coche.lee_cuentakilometros()
    
    # Intentamos retroceder el odómetro:
    mi_nuevo_coche.update_cuentakilomentros(10)

    Este coche ha recorrido 23 kilómetros.
    ¡No puedes retroceder el cuentakilómetros!

Ahora `update_cuentakilomentros()` comprueba que la nueva lectura tiene
sentido antes de modificoche el atributo. Si el valor proporcionado es
**mayor o igual** que el kilometraje existente, se actualiza. Si es
**menor**, se muestra una advertencia.


<a id="org2041a3e"></a>

## Forma 3 — Incrementar un atributo mediante un método

A veces querrás **sumar** una cantidad al valor de un atributo, en lugar
de asignarle un valor completamente nuevo.

Ejemplo: compramos un coche usado y le hacemos 100 millas entre la
compra y el registro.

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
    		print(f"Este coche ha recorrido {self.cuentakilomentros_lectura} kilómetros.")
    
    	def update_cuentakilomentros(self, kilometraje):
    		"""
    		Establece la lectura del cuentakilómetros al valor dado.
    		Rechaza el cambio si intenta retroceder el cuentakilómetros.
    		"""
    		if kilometraje >= self.cuentakilomentros_lectura:
    			self.cuentakilomentros_lectura = kilometraje
    		else:
    			print("¡No puedes hacer retroceder el cuentakilómetros!")
    
    	def incrementa_cuentakilomentros(self, miles):
    		"""Suma la cantidad dada a la lectura del cuentakilómetros."""
    		self.cuentakilomentros_lectura += miles
    
    mi_coche_usado = Coche('opel', 'corsa', 2019)
    print(mi_coche_usado.nombra_descriptivamente())
    
    mi_coche_usado.update_cuentakilomentros(23_500)
    mi_coche_usado.lee_cuentakilometros()
    
    mi_coche_usado.incrementa_cuentakilomentros(100)
    mi_coche_usado.lee_cuentakilometros()

    2019 Opel Corsa
    Este coche ha recorrido 23500 kilómetros.
    Este coche ha recorrido 23600 kilómetros.


### Qué ocurre aquí

-   `incrementa_cuentakilomentros()` recibe un número de millas y **suma** ese
    valor a `self.cuentakilomentros_lectura`.
-   Primero creamos un coche usado (`mi_coche_usado`).
-   Le asignamos 23.500 millas con `update_cuentakilomentros()`.
-   Luego llamamos a `incrementa_cuentakilomentros(100)` para añadir las 100
    millas recorridas entre la compra y el registro.

> **NOTA:** Puedes usar métodos como estos para controlar cómo los
> usuarios de tu programa actualizan valores como el cuentakilómetros,
> pero cualquier persona con acceso al programa puede asignar
> directamente cualquier valor accediendo al atributo. La seguridad
> efectiva requiere una atención extrema al detalle, además de las
> comprobaciones básicas mostradas aquí.


<a id="orgff15180"></a>

# Resumen de Conceptos

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left"><b>Concepto</b></td>
<td class="org-left"><b>Descripción</b></td>
<td class="org-left"><b>Ejemplo</b></td>
</tr>


<tr>
<td class="org-left">:---</td>
<td class="org-left">:---</td>
<td class="org-left">:---</td>
</tr>


<tr>
<td class="org-left"><b>Atributo con parámetro</b></td>
<td class="org-left">Se pasa al crear la instancia</td>
<td class="org-left"><code>self.fabricante = fabricante</code></td>
</tr>


<tr>
<td class="org-left"><b>Atributo por defecto</b></td>
<td class="org-left">Se define en <code>__init__()</code> sin parámetro</td>
<td class="org-left"><code>self.cuentakilomentros_lectura = 0</code></td>
</tr>


<tr>
<td class="org-left"><b>Acceso directo</b></td>
<td class="org-left">Modificoche atributo con notación de punto</td>
<td class="org-left"><code>coche.cuentakilomentros_lectura = 23</code></td>
</tr>


<tr>
<td class="org-left"><b>Método setter</b></td>
<td class="org-left">Método que asigna un nuevo valor</td>
<td class="org-left"><code>update_cuentakilomentros(23)</code></td>
</tr>


<tr>
<td class="org-left"><b>Método incremento</b></td>
<td class="org-left">Método que suma al valor existente</td>
<td class="org-left"><code>incrementa_cuentakilomentros(100)</code></td>
</tr>


<tr>
<td class="org-left"><b>Lógica de protección</b></td>
<td class="org-left">Validación dentro del setter</td>
<td class="org-left"><code>if kilometraje &gt;</code> self.cuentakilomentros<sub>lectura</sub>=</td>
</tr>
</tbody>
</table>

