from django.urls import path, include
from apps.rutina import views

urlpatterns = [
    path('', views.RutinaListView.as_view(), name='index_rutina'),
    path('cargar_rutina', views.RutinaCreateView.as_view(), name='cargar_rutina'),
    path('editar_rutina/<int:pk>/', views.RutinaUpdateView.as_view(), name='editar_rutina'),
    path('confirmar_eliminar_rutina/<int:pk>/', views.RutinaDeleteView.as_view(), name='confirmar_eliminar_rutina'),
]