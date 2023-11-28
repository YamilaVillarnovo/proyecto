from django.db import models
from django.utils import timezone

class alumnoTable(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField()
    correo_electronico = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
