from django.contrib import admin
from apps.horarios.models import Horarios

# Register your models here.
    
class HorariosAdmin(admin.ModelAdmin):
    list_display = ('profesor', 'rutina', 'dias_semana', 'hora_inicio', 'hora_fin')

admin.site.register(Horarios, HorariosAdmin)

# Register your models here.
