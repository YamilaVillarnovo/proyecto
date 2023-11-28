from django.db import models
from apps.alumno.models import alumnoTable
from apps.rutina.models import Rutina
from django.utils import timezone


class Reservas(models.Model):
    alumno = models.ForeignKey(alumnoTable, on_delete=models.CASCADE)
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    fecha_hora_reserva = models.DateTimeField()
    estado_reserva = models.CharField(max_length=50)
    
    #Función para que aparezca como reservado o cancelado dependiendo la hora seleccionada
    def save(self, *args, **kwargs):
        if self.fecha_hora_reserva <= timezone.now():
            self.estado_reserva = "cancelado"
        else:
            self.estado_reserva = "reservado"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Reserva de {self.alumno.nombre} {self.alumno.apellido} para {self.rutina.nombre} ({self.estado_reserva})'



# Create your models here.
