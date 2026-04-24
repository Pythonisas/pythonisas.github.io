---
title: "Práctica ML 1 — Predicción de precios de vivienda (Regresión)"
author: ["Pythonisas"]
date: "2026-04-24"
tags: ["prácticas", "machine-learning"]
url: "/ml-vivienda/"
---

# Práctica ML 1 — Predicción de precios de vivienda (Regresión)

![ML Houses](/images/ml-houses.jpg)

## Contexto (sin humo)
Vamos a construir un *mini-sistema* que, a partir de características simples de una vivienda, estime su precio.

Esto es *Machine Learning* en modo realista:
- no buscamos “la fórmula perfecta”,
- buscamos un modelo que *aproxime bien* y que sepamos *evaluar*.

## Objetivo
En esta práctica vais a:
1. Cargar un dataset pequeño (CSV) de viviendas.
2. Preparar los datos (limpieza + columnas).
3. Entrenar *dos modelos*:
   - `LinearRegression` (modelo base, rápido y fácil de interpretar)
   - `RandomForestRegressor` (modelo más potente, no lineal)
4. Evaluarlos con métricas de regresión (`MAE` y `RMSE`).
5. Hacer predicciones desde la terminal.

## Audiencia / forma de trabajo
- Trabajo en **tríos**.
- Entregable: una carpeta/repo con scripts ejecutables en terminal.
- Se valora claridad, orden y que el programa no “reviente” al primer error.

## Requisitos
- Python 3.10+ (o el que use vuestro entorno)
- Entorno virtual (`venv`)
- Librerías:
  - `pandas`
  - `scikit-learn`
  - `joblib` (para guardar modelo, **bonus**)

## Estructura de carpetas (lo que debéis entregar)
Cread esta estructura:

```text
ml-vivienda/
├─ data/
│  ├─ viviendas.csv
├─ src/
│  ├─ train_incompleto.py
│  ├─ predict_incompleto.py
│  ├─ features.py
│  └─ utils.py
├─ models/                  (se crea al entrenar)
│  ├─ model.joblib          (bonus)
│  └─ metadata.json         (bonus)
├─ README.org
└─ requirements.txt
```

## Dataset sugerido (pequeño y entendible)
Usaremos un CSV con columnas típicas (inventadas o semi-realistas):

- `m2` (metros cuadrados) → número
- `habitaciones` → entero
- `banos` → entero
- `zona` → categoría (por ejemplo: `centro`, `sur`, `norte`, `este`, `oeste`)
- `antiguedad` → años
- `precio` → *target* (lo que predecimos)

### Ejemplo de filas
```text
m2,habitaciones,banos,zona,antiguedad,precio
65,2,1,centro,30,210000
80,3,1,sur,15,165000
120,4,2,norte,5,320000
45,1,1,este,50,98000
```

## Flujo del proyecto (lo importante)
1. `train.py`:
   - Lee `data/viviendas.csv`
   - Separa `X` (features) y `y` (`precio`)
   - Crea un pipeline de preprocesado:
     - Numéricas: passthrough (o escalado opcional)
     - Categóricas: OneHotEncoding para `zona`
   - Entrena 2 modelos
   - Mide MAE y RMSE
   - Muestra resultados y decide “ganador”
   - (BONUS) Guarda el modelo ganador en `models/model.joblib`

2. `predict.py`:
   - Carga el modelo guardado
   - Pide por terminal los datos de una vivienda
   - Predice y muestra el precio estimado

## Importante: evaluación (métricas)
- `MAE` (Mean Absolute Error): “de media, ¿cuánto me equivoco en euros?”
- `RMSE` (Root Mean Squared Error): penaliza más los errores grandes.

## Entregables
- Código fuente completo:
  - `src/train.py` (a partir de `train_incompleto.py`)
  - `src/predict.py` (a partir de `predict_incompleto.py`)
- `requirements.txt`
- Un `README.org` explicando:
  - cómo crear el entorno
  - cómo entrenar
  - cómo predecir
  - resultados obtenidos (MAE/RMSE de ambos modelos)

## Rúbrica (10 puntos)
| Criterio | Puntos | Qué se espera |
|---------|--------|---------------|
| Carga dataset + validaciones | 2 | Maneja errores de archivo/columnas |
| Preprocesado correcto | 2 | OneHot para zona + separación X/y |
| Entrenamiento 2 modelos | 2 | LinearRegression + RandomForestRegressor |
| Evaluación correcta | 2 | MAE y RMSE con train/test split |
| Script predict por terminal | 2 | `input()` + predicción sin romper |
| BONUS: persistencia | +1 | Guardar/cargar modelo con `joblib` |

---

# Archivos de partida (esqueleto incompleto)
A continuación tienes los ficheros en “modo incompleto”. Los huecos marcados con `___` son para completar.

## `requirements.txt`
```text
pandas
scikit-learn
joblib
```

## `src/utils.py`
```python
from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"

def ensure_dirs() -> None:
    """Crea carpetas necesarias si no existen."""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
```

## `src/features.py`
```python
FEATURES = ["m2", "habitaciones", "banos](#)
