from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.profesor.models import profesor
from apps.profesor.forms import ProfesorForm
from django.urls import reverse_lazy

class ProfesorListView(ListView):
    model = profesor
    template_name = 'profesor/index_profesor.html'
    context_object_name = 'profesores'

class ProfesorCreateView(CreateView):
    model = profesor
    form_class = ProfesorForm
    template_name = 'profesor/cargar_profesor.html'
    success_url = reverse_lazy('index_profesor')

class ProfesorUpdateView(UpdateView):
    model = profesor
    form_class = ProfesorForm
    template_name = 'profesor/editar_profesor.html'
    success_url = reverse_lazy('index_profesor')

class ProfesorDeleteView(DeleteView):
    model = profesor
    template_name = 'profesor/confirmar_eliminar_profesor.html'
    success_url = reverse_lazy('index_profesor')
