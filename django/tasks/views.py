#views es la logica, lo que se manda al usuario
# los emplates son la estructura, rabaja con datos dinamicos

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def holamundo(request):
    return render(request,'singup.html', {
        'form': UserCreationForm
    })