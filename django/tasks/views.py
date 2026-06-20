#views es la logica, lo que se manda al usuario
# los emplates son la estructura, rabaja con datos dinamicos

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
# nombre de la funcion
def home(request):
    return render(request,'home.html') # nombre del archivo a renderizar

def singup(request):
    return render(request,'singup.html')