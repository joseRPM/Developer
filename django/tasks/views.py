#views es la logica, lo que se manda al usuario
# los emplates son la estructura, rabaja con datos dinamicos

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Request es un objeto de djangousado cada vez que alguien hace una peticion HTTP al servidor 
#(entra una url y sale un html). Contiene informacion de la peticion. Quien la hizo, metodo de uso, que datos
#

# Create your views here.
# VISTAS (views) de la app task.
# Funciones de python (logica). Es lo que python ejecuta cuando se visita una url
#En este caso renderizar un HTML

def home(request): # Lo que entra, una peticion
    return render(request,'home.html') # nombre del archivo a renderizar (lo que sale)
    # la funcion reder recive la consulta y el nombre del HTML a renderizar

def signup_view(request):
    return render(request,'signup.html',{
        'form': UserCreationForm()
    })