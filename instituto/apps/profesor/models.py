from django.db import models
from django.utils import timezone

class profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()
    correo_electronico = models.EmailField()
    especializacion = models.CharField(max_length=100)
    disponibilidad = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
