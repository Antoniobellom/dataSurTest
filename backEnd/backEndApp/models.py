from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Aquí puedes añadir campos adicionales si los necesitas
    telefono = models.CharField(max_length=15, blank=True)
    # Asegúrate de completar la definición del campo 'telefono' y cualquier otro campo adicional

class UnidadEjercito(models.Model):
    nombre = models.CharField(max_length=100)
    fuerza = models.IntegerField()
    movimiento= models.IntegerField()
    costo= models.IntegerField()

    def __str__(self):
        return self.nombre
