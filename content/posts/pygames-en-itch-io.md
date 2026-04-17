+++
title = "Pygames en itch.io — ¡a Jugarr!"
author = ["Fénix"]
publishDate = 2026-04-17
tags = ["pygame", "juegos"]
url = "/pygames-itch-io/"
draft = false
+++

{{< figure src="/images/El-Cosmos-de-la-Modularidad-Arquitectura-para-videojuegos-Pygame.png" >}}

Pygame no es un juguete. Es una librería con la que se construyen juegos de verdad — juegos que puedes jugar en el navegador, descargar, compartir con tus amigos. Y muchos de ellos están publicados en [itch.io](https://itch.io), la plataforma indie por excelencia.

Si bien nosotris nos centraremos en las próximas semanas en el clásico 'space invaders / invasión alienígena...

En este artículo repasamos **9 proyectos hechos con Pygame** que puedes jugar, estudiar y usar como inspiración para tus propios juegos. Cada uno enseña algo diferente — desde física 2D hasta motores narrativos.

---


## 🪐 Project Space — Simulación orbital 2D {#project-space-simulación-orbital-2d}

[Project Space en pygame.org](https://www.pygame.org/project/4145) · [Buscar en itch.io](https://itch.io/search?q=Project+Space)

Un simulador de órbitas donde los cuerpos se atraen según la ley de gravedad. No hay enemigos ni puntuación — solo física pura y el placer de ver planetas girar.

> **¿Qué puedes aprender?**
>
> -   El **game loop** clásico de Pygame: eventos → actualizar → dibujar
> -   Vectores de velocidad y aceleración (física 2D)
> -   Uso de `delta time` para que la simulación sea fluida en cualquier máquina


## 🚀 Flyre — Shoot'em up de game jam {#flyre-shoot-em-up-de-game-jam}

[Flyre en pygame.org](https://www.pygame.org/project/5523) · [Buscar en itch.io](https://itch.io/search?q=Flyre)

Un shoot'em up vertical nacido en una game jam y pulido después. Oleadas de enemigos, disparos, explosiones — el clásico arcade llevado a Pygame.

> **¿Qué puedes aprender?**
>
> -   `pygame.sprite.Group()` para gestionar decenas de sprites sin perder el control
> -   Scrolling de fondo para crear sensación de movimiento
> -   Cómo una game jam te obliga a priorizar: MVP primero, mejoras después


## 🧱 ArkaPygame — Colisiones y dificultad {#arkapygame-colisiones-y-dificultad}

[ArkaPygame en pygame.org](https://www.pygame.org/project/4891) · [Buscar en itch.io](https://itch.io/search?q=ArkaPygame)

Un clon de Arkanoid: pelota, pala, ladrillos. Simple en concepto, rico en mecánicas — cada nivel sube la dificultad.

> **¿Qué puedes aprender?**
>
> -   Detección de colisiones con `pygame.Rect.colliderect()`
> -   Curvas de dificultad: cómo hacer que cada nivel sea un poco más difícil
> -   Matemáticas con rectángulos: rebotes, ángulos, velocidad


## 🎁 Don't Touch My Presents — Sprint 72h → MVP {#don-t-touch-my-presents-sprint-72h-mvp}

[Don't Touch My Presents en pygame.org](https://www.pygame.org/project/5643) · [Buscar en itch.io](https://itch.io/search?q=Don't+Touch+My+Presents)

Un micro-arcade navideño creado en 72 horas. Defiende tus regalos de los ladrones. Pequeño, divertido, terminado.

> **¿Qué puedes aprender?**
>
> -   La mentalidad **MVP**: ¿qué es lo mínimo que necesita tu juego para ser jugable?
> -   Desarrollo bajo presión de tiempo — priorizar mecánicas sobre polish
> -   Que un juego terminado y pequeño vale más que un juego ambicioso sin acabar


## 🧙 Skeletris — Roguelike con inventario en rejilla {#skeletris-roguelike-con-inventario-en-rejilla}

[Skeletris en pygame.org](https://www.pygame.org/project/4506) · [Buscar en itch.io](https://itch.io/search?q=Skeletris)

Un roguelike donde la gestión del inventario es parte del gameplay. Rejilla tipo Tetris para organizar tus objetos — cada decisión importa.

> **¿Qué puedes aprender?**
>
> -   Inventario basado en rejilla (grid): matrices 2D en Python aplicadas al juego
> -   Generación procedural de mazmorras
> -   Máquinas de estado para controlar las fases del juego (explorar, combatir, inventario)


## 🐱 stuntcat — Git y trabajo en equipo {#stuntcat-git-y-trabajo-en-equipo}

[stuntcat en pygame.org](https://www.pygame.org/project/4266) · [stuntcat en itch.io](https://pygame.itch.io/)

El juego oficial de la comunidad Pygame. Un gato acróbata que esquiva objetos. Pero lo interesante no es solo el juego — es **cómo se hizo**: colaboración abierta en GitHub, con contribuciones de decenas de personas.

> **¿Qué puedes aprender?**
>
> -   Flujo de trabajo con **Git**: branches, pull requests, code review
> -   Cómo contribuir a un proyecto open source real
> -   Estructura de un proyecto Pygame profesional: carpetas, assets, tests


## 🧠 The N — Motor narrativo {#the-n-motor-narrativo}

[The N en pygame.org](https://www.pygame.org/project/3085) · [Buscar en itch.io](https://itch.io/search?q=The+N)

Un juego narrativo donde la historia se cuenta a través de texto y decisiones. Lo fascinante es la arquitectura: el **motor** (código) está separado del **contenido** (historia).

> **¿Qué puedes aprender?**
>
> -   Separar el motor del contenido: el código no cambia cuando cambias la historia
> -   Diseño dirigido por datos (data-driven): la narrativa vive en ficheros, no en el código
> -   Cómo Pygame puede servir para más que juegos de acción


## 🧩 Pygame Weapons Source Code — Módulos reutilizables {#pygame-weapons-source-code-módulos-reutilizables}

[Pygame Weapons en pygame.org](https://www.pygame.org/project/5540) · [Buscar en itch.io](https://itch.io/search?q=Pygame+Weapons)

No es un juego completo — es una colección de **sistemas de armas** listos para usar en tus propios proyectos. Espadas, proyectiles, escudos, cada uno como un módulo independiente.

> **¿Qué puedes aprender?**
>
> -   Diseño modular: cada arma es un módulo que puedes importar y reutilizar
> -   Patrones de diseño aplicados a juegos (Strategy, Factory)
> -   Cómo escribir código que otros puedan usar — documentación y API limpia


## 🐱 El ecosistema Pygame — más allá de un solo juego {#el-ecosistema-pygame-más-allá-de-un-solo-juego}

[Página de pygame en itch.io](https://pygame.itch.io/) · [stuntcat en pygame.org](https://www.pygame.org/project/4266)

stuntcat no es solo un juego — es la puerta de entrada al ecosistema [pygame-community](https://github.com/pygame-community) en GitHub. Una organización con decenas de proyectos, herramientas y recursos mantenidos por la comunidad.

Si te gusta Pygame y quieres ir más allá de tus propios proyectos, este es el sitio donde contribuir, aprender y conectar con otros desarrolladores.

---


## ¿Qué tienen en común estos juegos? {#qué-tienen-en-común-estos-juegos}

| **Juego**               | **Concepto clave**                 |
|-------------------------|------------------------------------|
| Project Space           | Game loop + física 2D              |
| Flyre                   | Sprite groups + scrolling          |
| ArkaPygame              | Colisiones + dificultad progresiva |
| Don't Touch My Presents | MVP en tiempo limitado             |
| Skeletris               | Inventario en rejilla + estado     |
| stuntcat                | Git + colaboración open source     |
| The N                   | Motor vs contenido (data-driven)   |
| Pygame Weapons          | Módulos reutilizables              |

Todos empezaron como un fichero `.py` vacío. Todos terminaron publicados y jugables.

---


## Tu turno: publica en itch.io {#tu-turno-publica-en-itch-dot-io}

Si ya sabes hacer un juego con Pygame, estás más cerca de lo que crees de publicarlo. Los pasos son:

1.  **Empaqueta tu juego** como ejecutable con PyInstaller ([ver nuestro tutorial](/pyinstallerexe/))
2.  **Crea una cuenta** en [itch.io](https://itch.io) (es gratis)
3.  **Sube tu juego**: arrastra el `.zip` con tu ejecutable y assets
4.  **Escribe una página** con capturas de pantalla y descripción
5.  **Comparte el enlace** — tu juego ya está en internet

> **Recuerda:** No necesitas un juego perfecto. Necesitas un juego **terminado**. Los 9 juegos de este artículo empezaron igual que los tuyos — con un `pygame.init()` y una idea.

---

_Artículo elaborado con fines docentes — FP Informática_
