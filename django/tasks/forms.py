from django import forms
from .models import Task

#Estilizamos nuestros propios formularios desde aqui
class  taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['title','description','important']
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe el nombre de la tarea'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe la descripcion de la tarea'}),
            'important':forms.CheckboxInput(attrs={'class': 'form-check-input mx-auto d-block'}),
        }