# https://www.youtube.com/watch?v=wrSS9Tz2zqg&list=PLH4-zYHtDkEhWhWFf0LhbIYS0gbDOIfso&index=3&ab_channel=ThatPythonTeacher
# Para hacer el projecto con react native y django



"""
1.crear el django project

2. Algun problema de dependencias con REST_FRAMEWORK_JWT y la version DJANGO
Solucion del comentario de youtube que funciono:
Had same problem. Apparently smart_text is not supported by django 4.0 so 
i installed django 3.2.2 as in video and it started working. 
You can do it with pip install Django==3.2.2













"""











#-----------------------------------------
#-----------------------------------------
# Se puede instalar python desde la microsoft 
# store para evitar poner el PATH.



#-----------------------------------------
#-----------------------------------------
#   Los comandos para crear un entorno varian segun
#   el sistema operativo. Windows, MAC o Linux.
#
#   Lo primero es instalar el entorno virtual: 
#       pip install virtualenv
#
#   Luego crear el ambiente:
#       virtualenv env[nombre-del-dir]
#
#   Activar el ambiente:
#       ./env/Scripts/activate
#     --IMPORTANTE--: Esto hay que ejecutarlo siguiendo la ruta. DESDE AFUERA DONDE ESTA INSTALADO PYTHON.
#            Lo mejor seria ejecutarlo desde la carpeta del repo.
#


#-----------------------------------------
#-----------------------------------------
#   [Buena practica] Hacer el gitignore para [buscarlo en google gitIgnore]
#   que el archivo de env no se suba al repo.

#   [Buena practica] Se hace un archivo requirements.txt para el control de versionado.
#   Django==3.2.6 => version del tutorial.
#   luego se corre el comando: pip install -r requirements.txt
#   recordar correrlo dentro del entorno

#   Recordar acceder a la documentacion de Django.
#   Crear un proyecto de Django
#   En la terminal: django-admin startproject core .
#   recordar correrlo dentro del entorno

#   Iniciar el server de un proyecto de Django
#   En la terminal: python manage.py runserver
#   


#   Hacer las migraciones
#   En la terminal: python manage.py migrate
#   En la base se datos se aplican las  
#   


#   Para crear una app
#   En la terminal: python manage.py startapp [nombre-del-archivo]
#   Agregarlo en setting.py del core y en url
# 