from django.db import models

# Create your models here.
class Ubicacion(models.Model):
    nombre = models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 30)
    def __str__(self) -> str:
        return f"{self.nombre} {self.direccion}"

class Profesora(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Clase(models.Model):
    fecha = models.DateField(null = True)
    nombre = models.CharField(max_length = 20)
    def __str__(self) -> str:
        return f"{self.fecha} {self.nombre}"
