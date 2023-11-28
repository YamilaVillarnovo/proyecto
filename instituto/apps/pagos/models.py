from django.db import models
from django.utils import timezone
from apps.alumno.models import alumnoTable

class Pagos(models.Model):
    FORMADEPAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta crédito', 'Tarjeta Crédito'),
        ('tarjeta débito', 'Tarjeta Débito'),
        ('mercado pago', 'Mercado Pago'),
    ]
    alumno = models.ForeignKey(alumnoTable, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    metodo_pago = models.CharField(max_length=50, choices=FORMADEPAGO_CHOICES)

