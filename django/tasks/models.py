from django.db import models
from django.contrib.auth.models import User #tabla user
# Create your models here.
#tabla sql generada por python
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)      
    created = models.DateField(auto_now_add=True)
    datecompleted = models.DateField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)