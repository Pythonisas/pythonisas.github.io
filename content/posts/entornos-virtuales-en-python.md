+++
title = "Uso de entornos virtuales mágicos"
author = ["fenix"]
date = 2026-01-15T12:00:00+01:00
publishDate = 2026-01-15
url = "/entornos-virtuales/"
draft = false
+++

## ¿Por qué entornos virtuales?

Durante el desarrollo de aplicaciones en Python, pueden surgir problemas relacionados con el uso de diferentes versiones de bibliotecas. Por ejemplo, dos aplicaciones diferentes pueden necesitar la misma biblioteca, pero de diferentes versiones. O puede que necesites asegurar el funcionamiento correcto de una aplicación independientemente de las actualizaciones de la versión de la biblioteca que utiliza.

Para solucionar estos problemas, los desarrolladores idearon una forma interesante: **ejecutar cada aplicación con su propio conjunto de versiones de bibliotecas en entornos aislados**. De esta manera, un entorno virtual (_virtual environment_) en Python permite gestionar proyectos de forma aislada:

-   Cada proyecto puede tener sus propias dependencias.
-   Las dependencias de un proyecto no afectan a las dependencias de otro proyecto.

Usaremos el módulo **venv**, que viene integrado en Python desde la versión 3.3+ — no hay que instalar nada adicional.

> **Importante:** antes de empezar, debes tener instalado Python 3 y pip. Si usas Windows, reemplaza `pip3` por `pip` y `python3` por `python`.

---

## Creación de un proyecto

Empecemos creando un proyecto. Primero, crea una carpeta para el proyecto y accede a ella:

```bash
mkdir my_python_project
cd my_python_project
```

## Creación del entorno virtual

Crea un entorno virtual dentro de la carpeta del proyecto:

```bash
python3 -m venv venv
```

> Si encuentras un error relacionado con `ensurepip`, en Ubuntu/Debian ejecuta:
>
> `sudo apt-get install python3-venv -y`

Esto crea una carpeta `venv/` que contiene una copia del intérprete de Python y un directorio `lib/` donde se instalarán los paquetes de este proyecto — completamente aislados del sistema.

## Activación del entorno virtual

Para activar el entorno virtual en **Linux/macOS**:

```bash
source venv/bin/activate
```

En **Windows**:

```bash
venv\Scripts\activate
```

Cuando el entorno está activo, verás el nombre del entorno entre paréntesis al inicio del prompt:

```text
(venv) usuario@maquina:~/my_python_project$
```

## Comprobación de paquetes instalados

Comprueba los paquetes pip instalados dentro del entorno virtual:

```bash
pip3 list
```

La salida inicial incluye solo `pip` y `setuptools` — el entorno está limpio y aislado.

Instala un paquete de ejemplo:

```bash
pip3 install requests
```

Vuelve a comprobar:

```bash
pip3 list
```

Ahora verás `requests` y sus dependencias, instaladas solo dentro de este entorno.

## Salida del entorno virtual

Para salir (desactivar) el entorno virtual:

```bash
deactivate
```

El prompt vuelve a la normalidad — ya no estás dentro del entorno aislado.

## Exportar paquetes instalados (requirements.txt)

Para crear un archivo con la lista de paquetes instalados y sus versiones:

```bash
pip3 freeze > requirements.txt
```

Este fichero `requirements.txt` permite reproducir el mismo entorno en otra máquina.

## Importar paquetes en otro entorno

En otra máquina (o en un entorno nuevo), crea un nuevo entorno virtual, actívalo, e importa los paquetes:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Resumen de comandos

-   **Crear entorno** — `python3 -m venv venv`
-   **Activar (Linux/macOS)** — `source venv/bin/activate`
-   **Activar (Windows)** — `venv\Scripts\activate`
-   **Ver paquetes** — `pip3 list`
-   **Instalar paquete** — `pip3 install nombre`
-   **Exportar paquetes** — `pip3 freeze > requirements.txt`
-   **Importar paquetes** — `pip3 install -r requirements.txt`
-   **Desactivar** — `deactivate`

> **Recuerda:** `venv` es la herramienta nativa de Python 3 y es suficiente para la mayoría de proyectos. No necesitas instalar nada adicional.

---

_Artículo basado en [CodigoNautas — Qué son venv y virtualenv en Python](https://codigonautas.com/venv-virtualenv-python-como-utilizarlos/)_
