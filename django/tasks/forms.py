from django.forms import ModelForm
from .models import Task

  
class  taskform(ModelForm):
    class meta:
        model = Task
        fields= ['title','description','important']