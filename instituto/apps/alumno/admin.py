from django.contrib import admin
from apps.alumno.models import alumnoTable

# Register your models here.
    
class alumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_de_nacimiento', 'correo_electronico')

admin.site.register(alumnoTable, alumnoAdmin)

