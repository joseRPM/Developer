"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
#path: ruta
# Estas son las rutas que el navegador pide "localhost:8000/signup/" no son funciones ni archivos solo strings
# para decidir que VISTA (views) ejecutar
urlpatterns = [
    path('admin/', admin.site.urls),                   #panel de administrador
    path('', views.home,name='home'),
    path('signup/', views.signup_view,name='signup'),                               #Registro
    path('task/', views.task_view,name='task.url'),                                 #Tareas
    path('task_completed/', views.task_view_completed,name='task_completed'),       #Mostrar tareas completas
    path('logout/', views.cerrar_sesion,name='logout'),                             #Cerrar sesion
    path('signin/', views.signin,name='signin'),                                    #Ingresar sesion
    path('task/create/', views.create_task,name='task'),                            #Crear tareas
    path('task/<int:task_id>/', views.task_detail,name='task_detail'),              #Detalles de la tarea
    path('task/<int:task_id>/complete/', views.complete_task,name='complete_task'), #Marcar una tarea 
    path('task/<int:task_id>/delete/', views.delete_task,name='delete_task')        #Eliminar tarea
    ]