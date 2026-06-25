from django.contrib import admin
from .models import Task


class taskadmin(admin.ModelAdmin):  #va a heredar todo lo del modelo admin
    readonly_fields=("created", ) # una tupla, no me puede modificar

# Register your models here.
admin.site.register(Task, taskadmin)   


