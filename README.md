# L2Proyecto
# Crear un entorno virtual
python -m venv proyecto2

# Activar el entorno virtual (en Windows)
cd proyecto2
Scripts\activate

# Salir de la carpeta
cd ..

# Instalar Django
pip install django

# Verificar las dependencias instaladas
pip freeze

# Crear un nuevo proyecto Django
django-admin startproject helloworld

# Cambiar al directorio del proyecto
cd helloworld

# Crear una nueva aplicación dentro del proyecto
python manage.py startapp myhelloapp

# Agregar la aplicación al archivo settings.py
# settings.py
INSTALLED_APPS = [
    ...
    'myhelloapp',
]

# Crear las migraciones para la nueva aplicación
python manage.py makemigrations myhelloapp

# Aplicar las migraciones
python manage.py migrate

# Crear dos archivos HTML básicos en la carpeta de plantillas de la aplicación
# Crear un directorio "templates" en la carpeta de la aplicación "myhelloapp"
mkdir myhelloapp/templates

# Crear un archivo "template1.html" dentro del directorio "templates"
<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Template 1</title>
</head>
<body>
    <h1>Template 1</h1>
    <ul>
        <li><a href="{% url 'template2' %}">Ir al Template 2</a></li>
    </ul>
</body>
</html>

# Crear un archivo "template2.html" dentro del directorio "templates"
<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Template 2</title>
</head>
<body>
    <h1>Template 2</h1>
    <ul>
        <li><a href="{% url 'template1' %}">Ir al Template 1</a></li>
    </ul>
</body>
</html>

# Modificar views.py dentro de la aplicación para renderizar los archivos HTML
# views.py
from django.shortcuts import render

def template1(request):
    return render(request, 'template1.html')

def template2(request):
    return render(request, 'template2.html')

# Crear urls.py dentro de la aplicación para definir las rutas
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('template1/', views.template1, name='template1'),
    path('template2/', views.template2, name='template2'),
]

# Modificar urls.py en el directorio del proyecto para incluir las rutas de la aplicación
# urls.py
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myhelloapp/', include('myhelloapp.urls'))
]

# Ejecutar el servidor de desarrollo
python manage.py runserver

# Cerrar entorno virtual
deactivate

# Crear archivo requiremenst.txt
pip freeze > requirements.txt
