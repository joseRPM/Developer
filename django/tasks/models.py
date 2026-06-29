from django.db import models
from django.contrib.auth.models import User #tabla user

#tengo problemas con la version de django, metemos mano
from django.utils import timezone

# Create your models here.
#tabla sql generada por python
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)      
    created = models.DateTimeField(auto_now_add=timezone.now)
    datecompleted = models.DateTimeField(null=True,blank=True) #condicional solo para el admin
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    #modo cascada (eliminamos el usuario, se eliminan las tareas)

    #Lo que quiero ver el la seccion de task del administrados
    def __str__(self):
        return self.title + ' - by ' + self.user.username
# La tabla user ya existe, se creo al importar 'User' e ingresar usuarios