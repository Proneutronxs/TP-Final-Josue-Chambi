from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class clsPaquetes(models.Model):
    name = models.CharField(max_length=25)
    numero = models.IntegerField()
    version = models.CharField(max_length=5)
    documentacion = models.CharField(max_length=255)
    licencia = models.CharField(max_length=20)
    fecha = models.DateField()
    tamaño = models.CharField(max_length=20)
    imagen = models.CharField(max_length=500)    

class clsAcercade(models.Model):
    about = models.CharField(max_length=255)

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen =models.ImageField(upload_to='avatares', null=True, blank =True)

