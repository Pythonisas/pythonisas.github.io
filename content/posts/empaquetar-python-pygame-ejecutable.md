+++
title = "Empaquetar un juego Python+Pygame como ejecutable"
author = ["Fénix"]
date = 2026-03-15T12:00:00+01:00
publishDate = 2026-03-14
url = "/pyinstallerexe/"
draft = false
+++

## ¿Es posible? Sí, con PyInstaller {#es-posible-sí-con-pyinstaller}

**PyInstaller** analiza tu proyecto, detecta todas las dependencias
(incluyendo Pygame) y las empaqueta junto con el intérprete de Python
en un único binario autocontenido.

> No necesitas instalar Python en la máquina destino.


## Herramientas disponibles {#herramientas-disponibles}

| **Herramienta** | **Windows `.exe`** | **Linux binario** | **macOS `.app`** | **Notas**                    |
|-----------------|--------------------|-------------------|------------------|------------------------------|
| **PyInstaller** | Si                 | Si                | Si               | La más popular y documentada |
| **cx_Freeze**   | Si                 | Si                | Si               | Alternativa clásica          |
| **Nuitka**      | Si                 | Si                | Si               | Compila a C → más rápido     |

Este tutorial usa **PyInstaller** (KISS).


## Juego de ejemplo mínimo {#juego-de-ejemplo-mínimo}

```python
# Rationale: Snake game mínimo para demostrar el empaquetado con PyInstaller
# Version: 1.0
# Author: fenix & LLM friends
# License: GPL v3 - https://www.gnu.org/licenses/gpl-3.0.html

import pygame
import sys

# --- Constantes ---
ANCHO, ALTO = 640, 480
FPS         = 60
NEGRO       = (0,   0,   0)
VERDE       = (0, 200,   0)
TITULO      = "Mini Snake – fenix & LLM friends"

def inicializar():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(TITULO)
    return pantalla, pygame.time.Clock()

def procesar_eventos():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def dibujar(pantalla, pos):
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, VERDE, (*pos, 20, 20))
    pygame.display.flip()

def mover(pos, dx, dy):
    return (pos[0] + dx, pos[1] + dy)

def bucle_principal(pantalla, reloj):
    pos  = (ANCHO // 2, ALTO // 2)
    dx, dy = 4, 0
    teclas = {
        pygame.K_UP:    (0,  -4),
        pygame.K_DOWN:  (0,   4),
        pygame.K_LEFT:  (-4,  0),
        pygame.K_RIGHT: (4,   0),
    }
    while True:
        procesar_eventos()
        pulsadas = pygame.key.get_pressed()
        for tecla, (ndx, ndy) in teclas.items():
            if pulsadas[tecla]:
                dx, dy = ndx, ndy
        pos = mover(pos, dx, dy)
        dibujar(pantalla, pos)
        reloj.tick(FPS)

if __name__ == "__main__":
    pantalla, reloj = inicializar()
    bucle_principal(pantalla, reloj)
```

Guarda el archivo como `snake.py`.


## Instalar PyInstaller {#instalar-pyinstaller}

```bash
pip install pyinstaller
```

Comprueba la instalación:

```bash
pyinstaller --version
```


## Empaquetar — modo básico {#empaquetar-modo-básico}


### Un solo fichero (recomendado para distribuir) {#un-solo-fichero--recomendado-para-distribuir}

```bash
pyinstaller --onefile snake.py
```


### Con icono personalizado (`.ico` en Windows, `.icns` en macOS) {#con-icono-personalizado--dot-ico-en-windows-dot-icns-en-macos}

```bash
pyinstaller --onefile --icon=assets/icono.ico snake.py
```


### Sin ventana de consola (Windows — importante para juegos) {#sin-ventana-de-consola--windows-importante-para-juegos}

```bash
pyinstaller --onefile --noconsole snake.py
```


### Todo junto (caso habitual en juegos) {#todo-junto--caso-habitual-en-juegos}

```bash
pyinstaller --onefile --noconsole --icon=assets/icono.ico snake.py
```


## Estructura de directorios generada {#estructura-de-directorios-generada}

```text
proyecto/
├── snake.py
├── snake.spec          ← fichero de configuración reutilizable
├── build/              ← archivos temporales (ignorar en Git)
└── dist/
    └── snake           ← binario Linux  (o snake.exe en Windows)
```

Añade al `.gitignore`:

```text
build/
dist/
*.spec
```


## Incluir assets (imágenes, sonidos, fuentes) {#incluir-assets--imágenes-sonidos-fuentes}

Si el juego usa recursos externos hay que declararlos explícitamente.


### Opción A — línea de comandos {#opción-a-línea-de-comandos}

```bash
pyinstaller --onefile --noconsole \
  --add-data "assets/sprite.png:assets" \
  --add-data "assets/musica.ogg:assets" \
  snake.py
```

> **Sintaxis:** `origen:destino_dentro_del_paquete`
>
> En Windows usa `;` en lugar de `:`.


### Opción B — editar el fichero `.spec` (más limpio) {#opción-b-editar-el-fichero-dot-spec--más-limpio}

```python
# snake.spec  (fragmento relevante)
a = Analysis(
    ['snake.py'],
    datas=[
        ('assets/sprite.png', 'assets'),
        ('assets/musica.ogg', 'assets'),
    ],
    ...
)
```

Luego:

```bash
pyinstaller snake.spec
```


### Acceder a los assets desde el código {#acceder-a-los-assets-desde-el-código}

```python
# Rationale: localizar assets tanto en desarrollo como en el binario empaquetado
# Version: 1.0
# Author: fenix & LLM friends
# License: GPL v3

import sys
from pathlib import Path

def ruta_asset(nombre: str) -> Path:
    """Devuelve la ruta correcta del asset en cualquier entorno."""
    base = Path(getattr(sys, '_MEIPASS', Path(__file__).parent))
    return base / nombre

imagen = pygame.image.load(str(ruta_asset("assets/sprite.png")))
```

`sys._MEIPASS` es la carpeta temporal que PyInstaller crea en tiempo
de ejecución cuando el binario se ejecuta como `--onefile`.


## Compilar en Linux → binario Linux {#compilar-en-linux-binario-linux}

```bash
# En una máquina GNU/Linux:
pyinstaller --onefile --noconsole snake.py

# Resultado:
./dist/snake        # ELF binary, ejecutable nativo
```

```bash
chmod +x dist/snake
./dist/snake
```

> **Importante:** PyInstaller genera ejecutables **para la plataforma
> donde se ejecuta**. Para hacer un `.exe` necesitas ejecutarlo en
> Windows (o usar Wine / una VM / GitHub Actions).


## Cross-compilation con GitHub Actions (avanzado) {#cross-compilation-con-github-actions--avanzado}

```yaml
# .github/workflows/build.yml
name: Build executables

on: [push]

jobs:
  build-linux:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install pygame pyinstaller
      - run: pyinstaller --onefile --noconsole snake.py
      - uses: actions/upload-artifact@v4
        with:
          name: snake-linux
          path: dist/snake

  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: pip install pygame pyinstaller
      - run: pyinstaller --onefile --noconsole snake.py
      - uses: actions/upload-artifact@v4
        with:
          name: snake-windows
          path: dist/snake.exe
```

Con este workflow obtienes **ambos binarios** automáticamente en cada push.


## Alternativa: Nuitka (compilación real a C) {#alternativa-nuitka--compilación-real-a-c}

```bash
pip install nuitka

# Linux
python -m nuitka --onefile --enable-plugin=pygame snake.py

# Windows
python -m nuitka --onefile --windows-disable-console \
                 --enable-plugin=pygame snake.py
```

Nuitka compila Python a C y luego a binario nativo → **más rápido**
en ejecución, pero el proceso de compilación es más lento.


## Resumen {#resumen}

```text
pip install pyinstaller
pyinstaller --onefile --noconsole snake.py
→ dist/snake  (Linux) | dist/snake.exe (Windows)
```

| **Necesidad**            | **Opción recomendada**         |
|--------------------------|--------------------------------|
| Distribución simple      | `--onefile`                    |
| Juego sin consola        | `--noconsole`                  |
| Assets (imágenes, audio) | `--add-data` o fichero `.spec` |
| Multi-plataforma sin VM  | GitHub Actions                 |
| Máximo rendimiento       | Nuitka                         |

> _Tutorial generado con fines docentes — FP Informática_
>
> _Licencia: GPL v3 — <https://www.gnu.org/licenses/gpl-3.0.html>_
