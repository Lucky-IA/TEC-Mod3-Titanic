# Proyecto Titanic

TEC Monterrey - Machine Learning - Modulo 3

**[Alex Castro Gumiel](https://www.linkedin.com/in/alex-castro-gumiel/)**

## Entregable del Modulo

> La actividad consiste en refactorizar el código que realizaron en Google Colab para hacer predicciones del Titanic. Para su solución tengan en cuenta lo siguiente:

> - Su proyecto debe vivir en un repositorio de GitHub.
> - Deben convertir su notebook de Colab en scripts .py organizados en una estructura de directorio.
> - El producto final deber servir las inferencias de su modelo vía un servicio REST (usando FastAPI).
> - Deben seguir las buenas prácticas de desarrollo de software que hemos aprendido hasta el momento, a saber:
>   - Seguir los lineamientos de PEP8.
>   - Sus funciones y/o clases deben incluir docstrings.
>   - Su proyecto debe tener un pyproject.toml, README.md, .gitignore, etc.
>   - Incluir tests unitarios
>   - Desarrollar pipelines de procesamiento y/o entrenamiento.

## GitHub Repository

https://github.com/Lucky-IA/TEC-Mod3-Titanic

## Structure and Scripts

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

> Project Structure

    ├── data
    │   ├── clean
    │   ├── raw
    ├── models
    ├── notebooks
    ├── src
    │   ├── classifier
    │   ├── load
    │   ├── train
    │   ├── transform
    
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── requirements.txt

## Serve Model with FastAPI

> /src/titanic_main.py

## Good Development Practices

```
$ black /src/titanic_main.py

$ black /src/classifier/titanic_classifier.py
$ black /src/load/data_load.py
$ black /src/train/train_model.py
$ black /src/transform/transform_data.py
```
