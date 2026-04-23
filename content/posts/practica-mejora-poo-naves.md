+++
title = "Práctica 3.5 — Refactoriza el duelo de naves espaciales"
author = ["Jordi"]
date = 2026-04-14T12:00:00+02:00
publishDate = 2026-04-13
tags = ["prácticas"]
url = "/poo5/"
draft = false
+++

{{< figure src="/images/nostromo.png" >}}


## Descripcion {#descripcion}

Alguien ha escrito un **juego de combate espacial** increible. Tiene de todo: menu de acciones, IA enemiga, robo de combustible, maniobras evasivas y barras visuales de escudo. Es divertido, funciona y se nota que quien lo programo sabe lo que hace.

Pero hay un problema: **la clase `Nave` esta practicamente vacia**.

En esta practica vas a tomar ese juego como punto de partida y **mejorar su arquitectura POO** sin cambiar como funciona. El juego seguira siendo el mismo — pero su codigo sera mejor. Es lo que llamamos "refactorizar" el código fuente.

---


## El juego: Duelo de Naves Espaciales {#el-juego-duelo-de-naves-espaciales}

Antes de tocar nada, **juega**. Ejecuta el fichero y prueba las 4 opciones de combate:

```text
$ python3 duelo_naves.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ¡ALERTA DE COMBATE! NAVE PIRATA DETECTADA
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Capitán, nombre de su nave: FENIX

🚀 FENIX: [██████████] 100% | ⛽ Combustible: 100%
🏴‍☠️ CRUCERO PIRATA: [████████████] 120%
--------------------------------------------------
¿ÓRDENES?
1. DISPARAR (-10 comb. | -20 daño)
2. MEGA-LÁSER (-30 comb. | -50 daño)
3. REPARAR (+25 escudo | -15 comb.)
4. ESQUIVAR (Evita el siguiente golpe | -10 comb.)
```

Las mecanicas del juego:

-   **Menu de 4 opciones** — disparar, mega-laser, reparar, esquivar. Cada accion tiene coste de combustible
-   **IA enemiga** — el enemigo responde cada turno con daño variable (15-25%)
-   **Robo de combustible** — al disparar hay un 40% de probabilidad de succionar combustible al enemigo
-   **Esquivar** — maniobra evasiva que evita el siguiente golpe enemigo
-   **Barras visuales** — el escudo se muestra con una barra grafica `████████`

---


## El codigo fuente {#el-codigo-fuente}

Descarga el fichero de partida: [duelo_naves.py](/code/poo5/duelo_naves.py)

```python
#!/usr/bin/env python3
import random
import time

class Nave:
    def __init__(self, nombre, escudo, combustible):
        self.nombre = nombre
        self.escudo = escudo
        self.combustible = combustible

    def estado_visual(self):
        barra = "█" * (self.escudo // 10)
        return f"[{barra:<10}] {self.escudo}%"

def iniciar_duelo():
    print("\n" + "!"*50)
    print("   ¡ALERTA DE COMBATE! NAVE PIRATA DETECTADA")
    print("!"*50)

    nombre_usuario = input("Capitán, nombre de su nave: ").upper()
    jugador = Nave(nombre_usuario, 100, 100)
    enemigo = Nave("CRUCERO PIRATA", 120, 999)

    while jugador.escudo > 0 and enemigo.escudo > 0:
        # Interfaz de combate
        print(f"\n🚀 {jugador.nombre}: {jugador.estado_visual()} | ⛽ Combustible: {jugador.combustible}%")
        print(f"🏴‍☠️ {enemigo.nombre}: {enemigo.estado_visual()}")
        print("-" * 50)

        print("¿ÓRDENES?")
        print("1. DISPARAR (-10 comb. | -20 daño)")
        print("2. MEGA-LÁSER (-30 comb. | -50 daño)")
        print("3. REPARAR (+25 escudo | -15 comb.)")
        print("4. ESQUIVAR (Evita el siguiente golpe | -10 comb.)")

        opcion = input("\nSeleccione (1-4): ").strip()

        esquivando = False

        if opcion == "1":
            if jugador.combustible >= 10:
                jugador.combustible -= 10
                daño = 20
                enemigo.escudo -= daño
                print(f"🎯 ¡Impacto! El pirata sufre -{daño} de daño.")
                # BONUS: Robar combustible
                if random.random() < 0.4:
                    robo = random.randint(5, 15)
                    jugador.combustible = min(100, jugador.combustible + robo)
                    print(f"📦 ¡Has succionado {robo}% de combustible del enemigo!")
            else: print("⚠️ ¡Sin energía para disparar!")

        elif opcion == "2":
            if jugador.combustible >= 30:
                jugador.combustible -= 30
                enemigo.escudo -= 50
                print("⚡ ¡BUM! La mega-carga sacude al crucero pirata.")
            else: print("⚠️ Energía insuficiente para el Mega-Láser.")

        elif opcion == "3":
            if jugador.combustible >= 15:
                jugador.combustible -= 15
                jugador.escudo = min(100, jugador.escudo + 25)
                print("🛠️  Reparando planchas de casco...")
            else: print("⚠️ No hay energía para reparaciones.")

        elif opcion == "4":
            if jugador.combustible >= 10:
                jugador.combustible -= 10
                esquivando = True
                print("✈️  Maniobra evasiva iniciada.")
            else: print("⚠️ Demasiado pesado para esquivar.")

        else:
            print("❌ ERROR DE SISTEMA: Orden no válida.")
            continue # Salta el turno del enemigo si te equivocas de tecla

        # Turno del Enemigo
        if enemigo.escudo > 0:
            time.sleep(1)
            if esquivando:
                print("\n💨 ¡El pirata dispara pero fallas por los pelos!")
            else:
                ataque_enemigo = random.randint(15, 25)
                jugador.escudo -= ataque_enemigo
                print(f"\n💥 ¡EL PIRATA RESPONDE! Te quita {ataque_enemigo}% de escudo.")

        # Verificar combustible crítico
        if jugador.combustible <= 0:
            print("\n🪫 COMBUSTIBLE AGOTADO. Te has quedado a la deriva...")
            jugador.escudo = 0

    # Resultado final
    if jugador.escudo > 0:
        print(f"\n🏆 ¡VICTORIA! El espacio vuelve a ser seguro para la {jugador.nombre}.")
    else:
        print("\n💀 DERROTA. Tu nave se ha convertido en chatarra espacial.")

if __name__ == "__main__":
    iniciar_duelo()
```

---


## El problema: la clase es un cascaron vacio {#el-problema-la-clase-es-un-cascaron-vacio}

Observa la clase `Nave`. Solo tiene **dos metodos**: `__init__()` y `estado_visual()`. Eso es todo.

**Toda la logica del juego esta en una funcion procedural** (`iniciar_duelo()`), no encapsulada en metodos de clase. Los 4 criterios centrales de la P3.3 — `actualizar_escudo`, `recibir_daño`, `consumir_combustible` y `recargar` como **metodos de clase con `self`** — no existen como metodos. El escudo y el combustible se modifican directamente desde fuera del objeto:

```python
# Así está ahora (procedural — modificación directa):
enemigo.escudo -= daño
jugador.combustible -= 10
jugador.escudo = min(100, jugador.escudo + 25)
```

¿Por que esto es un problema? Porque cualquier parte del codigo puede romper el estado del objeto. No hay validaciones centralizadas, no hay proteccion. Si mañana otro programador toca el juego, podria poner `jugador.escudo = -500` sin que nadie proteste.

```python
# Así debería estar (POO — encapsulado en la clase):
enemigo.recibir_daño(daño)
jugador.consumir_combustible(10)
jugador.reparar_escudo(25)
```

La diferencia parece cosmetica, pero es **fundamental** en POO: cuando el comportamiento esta dentro de la clase, el objeto se protege a si mismo (validaciones, limites 0-100, mensajes). Cuando esta fuera, el objeto es solo un saco de datos.

---


## Objetivo de la practica {#objetivo-de-la-practica}

Tu mision es **refactorizar** la clase `Nave` para que encapsule toda la logica de combate. El juego debe seguir funcionando **exactamente igual**, pero ahora la clase tendra significado.

---


## Como mejorar: mueve la logica a la clase {#como-mejorar-mueve-la-logica-a-la-clase}

El juego ya tiene toda la logica. Solo necesitas **moverla dentro de la clase**. Aqui van las pistas:


### 1. Metodo `recibir_daño(self, puntos)` {#1-dot-metodo-recibir-daño--self-puntos}

Mueve la logica de restar escudo a un metodo:

```python
def recibir_daño(self, puntos):
    """Reduce el escudo en la cantidad de puntos de daño recibidos."""
    self.escudo -= puntos
    if self.escudo < 0:
        self.escudo = 0
```

Y luego en `iniciar_duelo()`, en vez de `enemigo.escudo -` daño=, llama:

```python
enemigo.recibir_daño(daño)
```


### 2. Metodo `consumir_combustible(self, cantidad)` {#2-dot-metodo-consumir-combustible--self-cantidad}

```python
def consumir_combustible(self, cantidad):
    """Reduce el combustible en la cantidad consumida."""
    self.combustible -= cantidad
    if self.combustible < 0:
        self.combustible = 0
```


### 3. Metodo `reparar_escudo(self, puntos)` {#3-dot-metodo-reparar-escudo--self-puntos}

```python
def reparar_escudo(self, puntos):
    """Suma puntos al escudo sin superar el 100%."""
    self.escudo = min(100, self.escudo + puntos)
```


### 4. Metodo `recargar(self, cantidad)` {#4-dot-metodo-recargar--self-cantidad}

```python
def recargar(self, cantidad):
    """Suma combustible sin superar el 100%."""
    self.combustible = min(100, self.combustible + cantidad)
```


### 5. Metodo `estado(self)` {#5-dot-metodo-estado--self}

Amplia `estado_visual()` para que tambien muestre el combustible:

```python
def estado(self):
    """Imprime estado completo de la nave."""
    print(f"Escudo: {self.escudo}% | Combustible: {self.combustible}%")
```

---


## Entrega {#entrega}

Sube tu fichero `duelo_naves_poo.py` refactorizado con:

-   [ ] La clase `Nave` con **al menos 5 metodos** (`__init__`, `estado_visual`, `recibir_daño`, `consumir_combustible`, `reparar_escudo`)
-   [ ] La funcion `iniciar_duelo()` usando **llamadas a metodos** en vez de modificacion directa de atributos
-   [ ] El juego **funciona exactamente igual** que antes al ejecutarlo

---


## BONUS — Para nota maxima {#bonus-para-nota-maxima}

| **Bonus**       | **Descripcion**                                                                                              | **Puntos** |
|-----------------|--------------------------------------------------------------------------------------------------------------|------------|
| `recargar()`    | Metodo para sumar combustible (con cap a 100%)                                                               | **+0.5**   |
| `__str__()`     | `print(mi_nave)` muestra nombre + escudo + combustible                                                       | **+0.5**   |
| `esta_viva()`   | Metodo que devuelve `True` si `escudo > 0` y `combustible > 0`. Usalo en el `while`                          | **+0.5**   |
| Mejora creativa | Añade una mecanica nueva (criticos, escudo regenerativo, tipos de nave...) encapsulada en un metodo de clase | **+0.5**   |

---


## Rubrica de evaluacion {#rubrica-de-evaluacion}

| **Criterio**                              | **Puntos** | **Descripcion**                                |
|-------------------------------------------|------------|------------------------------------------------|
| **`recibir_daño()` como metodo de clase** | 2          | Usa `self`, `-=`, proteccion `< 0`             |
| **`consumir_combustible()` como metodo**  | 2          | Usa `self`, `-=`, proteccion `< 0`             |
| **`reparar_escudo()` como metodo**        | 1.5        | Usa `self`, `min(100, ...)`                    |
| **`estado()` ampliado**                   | 1          | Muestra escudo Y combustible                   |
| **`iniciar_duelo()` usa metodos**         | 1.5        | No modifica atributos directamente             |
| **El juego funciona igual**               | 1          | Sin errores, misma experiencia de juego        |
| **Codigo limpio**                         | 1          | Indentacion, nombres claros, sin codigo muerto |

|                        |                 |
|------------------------|-----------------|
| **Practica base**      | **10**          |
| **Con BONUS completo** | **12** (max 10) |

---


## Conceptos clave que practicaras {#conceptos-clave-que-practicaras}

| **Concepto**             | **Donde lo ves**                                                      |
|--------------------------|-----------------------------------------------------------------------|
| **Encapsulacion**        | La logica de modificar escudo/combustible vive DENTRO de la clase     |
| **`self`**               | Todos los metodos acceden al estado del objeto via `self.atributo`    |
| **Proteccion de estado** | Los metodos validan limites (0-100) — el objeto se protege a si mismo |
| **Refactorización**      | Mejorar la estructura del codigo sin cambiar su comportamiento        |
| **`-=` y `min()`**       | Operadores de incremento/decremento con limites                       |

---

> _"Un buen juego merece una buena arquitectura. Tu nave ya vuela — ahora dale su armadura POO."_ 🚀
