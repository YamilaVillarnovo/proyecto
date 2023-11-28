from django.contrib import admin
from apps.reservas.models import Reservas

# Register your models here.
    
class ReservasAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'rutina', 'fecha_hora_reserva', 'estado_reserva')
    readonly_fields = ('estado_reserva',)  # Esto hace que el campo sea de solo lectura en el admin

admin.site.register(Reservas, ReservasAdmin)
# Register your models here.
