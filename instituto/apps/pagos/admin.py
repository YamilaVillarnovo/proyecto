from django.contrib import admin
from apps.pagos.models import Pagos

# Register your models here.
    
class PagosAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'monto', 'fecha_pago', 'metodo_pago')

admin.site.register(Pagos, PagosAdmin)
# Register your models here.