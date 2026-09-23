+++
title = "Práctica 1.5 — Academia Pythonisa V: Cazabugs"
author = ["Jordi"]
tags = ["prácticas"]
url = "/python5/"
draft = true
+++

## Misión: Cazar lo invisible {#misión-cazar-lo-invisible}

**Contexto mágico:** En los pasillos de la Academia viven unas criaturas diminutas que se cuelan en los programas: los **bugs**. Algunos son escandalosos y rompen el programa nada más empezar. Otros son silenciosos: el programa funciona... pero hace algo distinto de lo que querías. Esos son los peores.

Para cazarlos, la Academia te entrega tu primera herramienta profesional: **el depurador**. Con él puedes congelar el tiempo, avanzar tu programa línea a línea y mirar dentro de cada variable.

> Basado en el Capítulo 6 de _Inventa tus propios juegos de computadora con Python_ -- Al Sweigart ([Cap. 6: Usando el depurador](https://github.com/JaquerEspeis/inventar-con-python/blob/master/capitulo6.md)). El libro usa IDLE; aquí lo adaptamos al depurador de **Thonny**.

---


## Los problemas a resolver {#los-problemas-a-resolver}

1.  **Reconocer al bicho** — No todos los bugs son iguales:
    -   **Errores de sintaxis**: Python no entiende lo que has escrito. No arranca
    -   **Errores de ejecución**: arranca, pero se estrella a mitad (`TypeError`, `NameError`...)
    -   **Errores de lógica**: no se estrella nunca... pero el resultado está mal. **Ningún mensaje te avisa**

2.  **Ver lo que no se ve** — Un programa se ejecuta en milésimas de segundo. Necesitas **frenarlo** y ejecutarlo paso a paso

3.  **No perder la tarde** — Ir paso a paso por 1000 vueltas de un bucle es inhumano. Necesitas decirle al depurador: _para solo aquí_

---


## Tu kit de cazabugs: el depurador de Thonny {#tu-kit-de-cazabugs-el-depurador-de-thonny}

| **Botón / atajo**          | **Qué hace**                                                                       |
|----------------------------|------------------------------------------------------------------------------------|
| 🐞 _Depurar_ (`Ctrl+F5`)   | Ejecuta el programa bajo el depurador: se para en la primera línea                 |
| _Paso por encima_ (`F6`)   | Ejecuta la línea entera y pasa a la siguiente                                      |
| _Paso dentro_ (`F7`)       | Entra dentro de la línea: evalúa cada trozo de la expresión, o entra en tu función |
| _Paso fuera_               | Termina la función actual y vuelve a quien la llamó                                |
| _Continuar_ (`F8`)         | Sigue a velocidad normal hasta el siguiente punto de interrupción                  |
| _Detener_ (`Ctrl+F2`)      | Para el programa                                                                   |
| Clic en el número de línea | Pone (o quita) un **punto de interrupción**: un punto rojo                         |
| _Ver → Variables_          | Tabla con todas las variables y sus valores en cada momento                        |

💡 Si no ves los números de línea: _Herramientas → Opciones → Editor → Mostrar números de línea_.

---


## Desafío 1: Paso a paso por el Reino de Dragones {#desafío-1-paso-a-paso-por-el-reino-de-dragones}

Abre tu `dragones.py` de la práctica 1.4.

**Requisitos:**

-   Pulsa `Ctrl+F5`. El programa se para en la primera línea (resaltada)
-   Avanza con `F6` (_paso por encima_) y observa en qué orden se ejecutan las líneas. ¿Por qué se _salta_ los `def` la primera vez?
-   Cuando llegue a `numero_de_cueva = elegir_cueva()`, pulsa `F7` (_paso dentro_): ¡entras dentro de la función!
-   Con _Ver → Variables_ abierto, observa cómo aparece `cueva` y cómo desaparece al salir de la función

**Diagnóstico:** si al pulsar `F7` en `time.sleep(2)` no pasa nada especial, es normal: las funciones de Python no se abren, solo las tuyas.

---


## Desafío 2: Encuentra el bug {#desafío-2-encuentra-el-bug}

Descarga este programa: [sumas_con_bug.py](/code/python5/sumas_con_bug.py). Pregunta una suma y comprueba la respuesta... o eso debería hacer.

```python
# sumas_con_bug.py — Práctica 1.5: ¡este programa tiene un bug!
import random

numero1 = random.randint(1, 10)
numero2 = random.randint(1, 10)
print('¿Cuánto es ' + str(numero1) + ' + ' + str(numero2) + '?')
respuesta = input()
if respuesta == numero1 + numero2:
    print('¡Correcto!')
else:
    print('¡Nooo! La respuesta es ' + str(numero1 + numero2))
```

Ejecútalo con `F5` y responde **bien**. Verás algo así:

```text
¿Cuánto es 9 + 2?
11
¡Nooo! La respuesta es 11
```

No hay ningún mensaje de error. Es un **error de lógica**.

**Requisitos:**

-   Depura con `Ctrl+F5` y avanza hasta la línea del `if`
-   Ahí, pulsa `F7` varias veces: Thonny irá sustituyendo cada trozo de la condición por su valor, hasta que veas exactamente qué está comparando
-   Mira también el panel de variables: ¿qué tipo de valor hay en `respuesta`? ¿Y en `numero1`?
-   Corrige el bug y guarda el programa arreglado como `sumas.py`

**Diagnóstico:** si no lo ves, fíjate en las comillas. En el panel de variables, ¿qué hay en `respuesta`: `11` o `'11'`?

---


## Desafío 3: Puntos de interrupción {#desafío-3-puntos-de-interrupción}

Descarga [lanzar_moneda.py](/code/python5/lanzar_moneda.py). Lanza una moneda 1000 veces y va contando las caras.

```python
# lanzar_moneda.py — Práctica 1.5: puntos de interrupción
import random

print('Lanzaré una moneda 1000 veces. ¿Cuántas veces saldrá cara? (Pulsa Enter para empezar)')
input()
lanzamientos = 0
caras = 0
while lanzamientos < 1000:
    if random.randint(0, 1) == 1:
        caras = caras + 1
    lanzamientos = lanzamientos + 1

    if lanzamientos == 900:
        print('900 lanzamientos y ha salido cara ' + str(caras) + ' veces.')
    if lanzamientos == 100:
        print('En 100 lanzamientos, ha salido cara ' + str(caras) + ' veces.')
    if lanzamientos == 500:
        print('A mitad de camino, ha salido cara ' + str(caras) + ' veces.')

print()
print('De 1000 lanzamientos, ha salido cara ' + str(caras) + ' veces.')
print('¿Te has acercado?')
```

Ir paso a paso aquí son miles de clics. Mejor:

**Requisitos:**

-   Pon **tres puntos de interrupción** (clic en el número de línea) en los tres `print()` de dentro del bucle
-   Pulsa `Ctrl+F5` y luego `F8` (_Continuar_): el programa correrá a toda velocidad y **se parará solo** en cada punto rojo
-   En cada parada, apunta los valores de `lanzamientos` y `caras`
-   ¿En qué orden se para? ¿Por qué no es 100 → 500 → 900 si en el código el 900 está primero?

**Diagnóstico:** si el programa no se para en los puntos rojos, comprueba que has usado `Ctrl+F5` (depurar) y no `F5` (ejecutar).

---


## Entrega {#entrega}

```text
PRACTICA1.5/
+-- sumas.py                 <-- el programa arreglado
+-- bitacora.md              <-- tu bitácora de caza (ver abajo)
+-- captura_paso_dentro.png  <-- Desafío 2: Thonny mostrando la comparación que falla
+-- captura_breakpoints.png  <-- Desafío 3: parado en un punto de interrupción
```

Súbela al **servidor SFTP del aula** (`put -r PRACTICA1.5`).

**La bitácora de caza** (`bitacora.md`) tiene una ficha por cada bug del Desafío 2, y otra por **un bug real tuyo** de cualquier práctica anterior:

```text
## Bug: ...
- Síntoma: qué veía (o qué no veía)
- Tipo: sintaxis / ejecución / lógica
- Hipótesis: qué creía que pasaba
- Lo que vi en el depurador: ...
- Solución: ...
```

Requisitos funcionales:

-   [ ] `sumas.py` dice "¡Correcto!" cuando la respuesta es correcta
-   [ ] La bitácora tiene al menos 2 fichas completas
-   [ ] Las capturas muestran el depurador en acción
-   [ ] Anotados los valores de `lanzamientos` y `caras` en las tres paradas

---


## Explica tu código {#explica-tu-código}

(En esta práctica, lo incluyes en `bitacora.md`.)

1.  ¿Qué diferencia hay entre _paso por encima_ (`F6`) y _paso dentro_ (`F7`)?
2.  ¿Por qué el bug del Desafío 2 no daba ningún mensaje de error?
3.  ¿Por qué el depurador se paraba antes en el 100 que en el 900?

---


## Rúbrica por competencias {#rúbrica-por-competencias}

| **Criterio**                      | **Hechicería (9-10)**                                           | **Aprendizaje (6-8)**                           | **Iniciación (0-5)** | **Peso** |
|-----------------------------------|-----------------------------------------------------------------|-------------------------------------------------|----------------------|----------|
| **Uso del depurador paso a paso** | Usa `F6` y `F7` con intención, sabe entrar y salir de funciones | Avanza paso a paso pero sin entrar en funciones | No usa el depurador  | **25%**  |
| **Caza del bug**                  | Lo encuentra con el depurador y lo corrige con `int()`          | Lo corrige pero sin usar el depurador           | No lo corrige        | **25%**  |
| **Puntos de interrupción**        | Tres puntos, valores anotados, explica el orden                 | Usa puntos pero no anota o no explica           | No los usa           | **20%**  |
| **Bitácora de caza**              | Fichas completas, incluido un bug real propio                   | Fichas incompletas o sin bug propio             | Sin bitácora         | **20%**  |
| **Explica tu código**             | Respuestas claras con ejemplos                                  | Correctas pero vagas                            | Sin respuestas       | **10%**  |

---


## Bonus (hasta +1.5) {#bonus--hasta-plus-1-dot-5}

| **Bonus**      | **Descripción**                                                                                                       | **Puntos** |
|----------------|-----------------------------------------------------------------------------------------------------------------------|------------|
| Bug plantado   | Mete un error de lógica en tu `dragones.py` y pásaselo a otra persona para que lo cace con el depurador (documéntalo) | **+1.0**   |
| Moneda trucada | Modifica `lanzar_moneda.py` para que la cara salga el 70% de las veces (pista: `randint(1, 10)`)                      | **+0.5**   |

---


## Conceptos clave {#conceptos-clave}

| **Concepto**                | **Dónde lo ves**                                              |
|-----------------------------|---------------------------------------------------------------|
| **Error de sintaxis**       | Python no arranca: `SyntaxError`                              |
| **Error de ejecución**      | Se estrella a mitad: `TypeError`, `NameError`, `ValueError`   |
| **Error de lógica**         | Funciona, pero mal: `'11' == 11` es `False` y no avisa        |
| **Depurador**               | Ejecuta el programa bajo tu control (`Ctrl+F5`)               |
| **Paso a paso**             | `F6` por encima, `F7` por dentro                              |
| **Punto de interrupción**   | Punto rojo: _para aquí_ (`F8` para llegar hasta él)           |
| **Inspección de variables** | _Ver → Variables_: el contenido de cada caja en cada instante |

---

> _"El ordenador hace exactamente lo que le dices. El bug no está en la máquina: está en la distancia entre lo que dijiste y lo que querías decir."_
