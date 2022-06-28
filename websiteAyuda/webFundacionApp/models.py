from django.db import models

# Create your models here.

class Residente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    rut = models.CharField(max_length=10)
    contacto = models.CharField(max_length=50)
    enfermedades = models.CharField(max_length=300)
    observaciones = models.CharField(max_length=300)
    
class Aporte(models.Model):
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero = models.IntegerField()
    residencia = models.CharField(max_length=50)
    monto  = models.IntegerField()
    fecha = models.CharField(max_length=50)
    
    
    
    