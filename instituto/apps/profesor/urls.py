from django.urls import path
from apps.profesor import views

urlpatterns = [
    path('', views.ProfesorListView.as_view(), name='index_profesor'),
    path('cargar_profesor', views.ProfesorCreateView.as_view(), name='cargar_profesor'),
    path('editar_profesor/<int:pk>/', views.ProfesorUpdateView.as_view(), name='editar_profesor'),
    path('confirmar_eliminar_profesor/<int:pk>/', views.ProfesorDeleteView.as_view(), name='confirmar_eliminar_profesor'),
    # Otras URLs que puedas necesitar para tu app de profesores
]

