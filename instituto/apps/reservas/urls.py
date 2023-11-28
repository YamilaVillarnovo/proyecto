from django.urls import path
from apps.reservas import views

urlpatterns = [
    path('', views.ReservaListView.as_view(), name='index_reserva'),
    path('cargar_reserva', views.ReservaCreateView.as_view(), name='cargar_reserva'),
    path('editar_reserva/<int:pk>/', views.ReservaUpdateView.as_view(), name='editar_reserva'),
    path('confirmar_eliminar_reserva/<int:pk>/', views.ReservaDeleteView.as_view(), name='confirmar_eliminar_reserva'),
    # Otras URLs que puedas necesitar para tu app de reservas
]
