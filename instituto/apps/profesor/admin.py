from django.contrib import admin
from apps.profesor.models import profesor

# Register your models here.

class profesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_de_nacimiento', 'correo_electronico', 'especializacion','disponibilidad')


admin.site.register(profesor, profesorAdmin)
