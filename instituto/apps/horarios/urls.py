from django.urls import path, include
from apps.horarios import views

urlpatterns = [
    path('', views.HorarioListView.as_view(), name='index_horarios'),
    path('cargar_horario/', views.HorarioCreateView.as_view(), name='cargar_horario'),
    path('exito/', views.pagina_exito, name='pagina_exito'),
    path('editar/<int:pk>/', views.HorarioUpdateView.as_view(), name='editar_horario'),
    path('confirmar_eliminar_horario/<int:pk>/', views.HorarioDeleteView.as_view(), name='confirmar_eliminar_horario'),
]