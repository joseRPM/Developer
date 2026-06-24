#views es la logica, lo que se manda al usuario
# los emplates son la estructura, rabaja con datos dinamicos
# Request es un objeto de django usado cada vez que alguien hace una peticion HTTP al servidor 
#lo que python ejecuta cuando se visita una url
#En este caso renderizar un HTML

from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout   
from django.db import IntegrityError




def home(request): # Lo que entra, una peticion
    return render(request,'home.html') # nombre del archivo a renderizar (lo que sale)
    # la funcion reder recive la consulta y el nombre del HTML a renderizar


# Vista para crear usuarios (funcionando)
def signup_view(request):

    if request.method == 'GET':
        return render(request,'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)                # En la cokies aparece session id para colocar datos del usuario
                return redirect('task.url')         #usuario creado exitosamente y redirecciona
            except IntegrityError:
                return render(request,'signup.html',{
                'form': UserCreationForm,
                'error': 'El usuario ya existe'
                })
            
        return render(request,'signup.html',{
            'form': UserCreationForm,
            'error': 'La contraseña no coincide'
        })
    
def task_view(request):
    return render(request,'task.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

