#views es la logica, lo que se manda al usuario
# los emplates son la estructura, rabaja con datos dinamicos
# Request es un objeto de django usado cada vez que alguien hace una peticion HTTP al servidor 
#lo que python ejecuta cuando se visita una url
#En este caso renderizar un HTML

from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate  
from django.db import IntegrityError
from .forms import taskform
from .models import Task




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
    tasks= Task.objects.all()

    return render(request,'task.html', {'tasks': tasks})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')
    #Los redirect reciben los nombres de las url no de los templates
    
def signin(request ):           # Ingresar con cuenta ya creada
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form': AuthenticationForm()
        })
    else: #verimicamos su existencia en la base de datos
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
            'form': AuthenticationForm,
            'error': 'usuario o constraseña incorrectas'
            })
        else:
            login(request,user )
            return redirect('task.url')  #Le puse este nombre (.url) para comprobar que se llama
                                         # a la url y no al html perse 



# GET peticion que hace el navegador cuando yo lo visito
def create_task(request):
    if request.method == "GET":
       return render(request, 'create_task.html',{
        'form': taskform()
    })
    #el boton envia una peticion tipo POST
    else: 
        #veo en consola el flujo de los datos
        #print(request.POST)
        try:
            form= taskform(request.POST)
            new_task= form.save(commit= False)
            new_task.user= request.user  #Necesitas el usuario de la tarea 
            print(new_task)
            new_task.save()
            return redirect('task.url')
        #cuando ocurr un error
        except ValueError:
           return render(request, 'create_task.html',{
           'form': taskform(),
           'error': 'Por favor ingrese un valor valido'})
