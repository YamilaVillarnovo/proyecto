from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.rutina.models import Rutina 
from apps.rutina.forms import RutinaForm 
from django.urls import reverse_lazy

class RutinaListView(ListView):
    model = Rutina
    template_name = 'rutina/index_rutina.html' 
    context_object_name = 'rutinas'

class RutinaCreateView(CreateView):
    model = Rutina
    form_class = RutinaForm
    template_name = 'rutina/cargar_rutina.html'  
    success_url = reverse_lazy('index_rutina')

class RutinaUpdateView(UpdateView):
    model = Rutina
    form_class = RutinaForm
    template_name = 'rutina/editar_rutina.html' 
    success_url = reverse_lazy('index_rutina')

class RutinaDeleteView(DeleteView):
    model = Rutina
    template_name = 'rutina/confirmar_eliminar_rutina.html' 
    success_url = reverse_lazy('index_rutina')
