from django.contrib import admin
from apps.rutina.models import Rutina

# Register your models here.
    
class RutinaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'nivel_dificultad', 'descanso_entre_series')

admin.site.register(Rutina, RutinaAdmin)

# Register your models here.
