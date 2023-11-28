from django.db import models
from apps.profesor.models import profesor
from apps.rutina.models import Rutina
from django.utils import timezone


class Horarios(models.Model):
    profesor = models.ForeignKey(profesor, on_delete=models.CASCADE)
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
 # Define las opciones para los días de la semana
    DIA_CHOICES = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miércoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sábado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    
    # Agrega un campo ManyToMany para los días de la semana
    dias_semana = models.CharField(max_length=50, choices=DIA_CHOICES)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()