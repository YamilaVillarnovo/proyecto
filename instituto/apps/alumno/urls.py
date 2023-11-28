from django.urls import path, include
from apps.alumno import views

urlpatterns = [
    path('', views.AlumnoListView.as_view(), name='index'),
    path('cargar_alumno/', views.AlumnoCreateView.as_view(), name='cargar_alumno'),
    path('exito/', views.pagina_exito, name='pagina_exito'),
    path('editar/<int:pk>/', views.AlumnoUpdateView.as_view(), name='editar_alumno'),
    path('eliminar/<int:pk>/', views.AlumnoDeleteView.as_view(), name='eliminar_alumno'),
]