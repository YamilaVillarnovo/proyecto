from django.db import models

# Create your models here.

class Rutina(models.Model):
    NIVEL_CHOICES = [
        ('leve', 'Leve'),
        ('moderada', 'Moderada'),
        ('energica', 'Energica'),
    ]
    DESCANSO_CHOISE = [
        ('5 min', '5 Minutos'),
        ('3 min', '3 Minutos'),
        ('2 min', '2 Minutos'),
        ('1 min', '1 Minuto'),
    ]
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    nivel_dificultad = models.CharField(max_length=50, choices=NIVEL_CHOICES)
    descanso_entre_series = models.CharField(max_length=50, choices=DESCANSO_CHOISE)
    
    def __str__(self):
        return f'{self.nombre} {self.descripcion}'