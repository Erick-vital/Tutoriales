# Python notas
algunas notas rapidas sobre python y conceptos que iremos aprendiendo en el camino

## Estructura de proyecto en python
De esta forma es como puede lucir una estructura de proyecto en python 

```
main_package/
    __init__.py
    file1.py
    file2.py
    file3.py
main.py
```

Algunos conceptos basicos que tenemos que conocer

### Archivo _ _init_ _.py
este archivo convierte el directorio en el que se encuentra en un modulo de python, dentro de este archivo deberemos inportar los archivos a
trabajar los cuales se convertiran en submodulos hijos del modulo padre (directorio)   

ejemplo de archivo __init__.py:
```
from . import file1, file2, file3
```

### Archivo main.py

## Instalar pip
comando para pip
```
sudo apt install python3-pip
```


## Entorno virtual virtualenv
comando para instalar virutalenv
```
sudo pip3 install virtualenv
```

Usa el siguiente comando para crear un entorno virtual
```
python -m venv venv
```
el primer parametro es el nombre del entorno y el segundo la ubicaci
