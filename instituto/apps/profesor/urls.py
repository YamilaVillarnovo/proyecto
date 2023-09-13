from django.urls import path, include
from apps.profesor import views

urlpatterns = [
    path('', views.index, name='index'),
]

