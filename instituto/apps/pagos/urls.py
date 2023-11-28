from django.urls import path
from apps.pagos import views

urlpatterns = [
    path('', views.PagoListView.as_view(), name='index_pagos'),
    path('cagar_pagos/', views.PagoCreateView.as_view(), name='carga_pagos'),
    path('editar_pagos/<int:pk>/', views.PagoUpdateView.as_view(), name='editar_pagos'),
    path('confirmar_eliminar_pagos/<int:pk>/', views.PagoDeleteView.as_view(), name='confirmar_eliminar_pagos'),
    path('exito/', views.pagina_exito, name='pagina_exito'),
]
