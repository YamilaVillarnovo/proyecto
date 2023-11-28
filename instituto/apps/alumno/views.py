from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.alumno.models import alumnoTable
from apps.alumno.forms import AlumnoForm
from django.urls import reverse_lazy

class AlumnoListView(ListView):
    model = alumnoTable
    template_name = 'alumno/index.html'
    context_object_name = 'alumnos'

class AlumnoCreateView(CreateView):
    model = alumnoTable
    form_class = AlumnoForm
    template_name = 'alumno/cargar_alumno.html'
    success_url = reverse_lazy('index')

class AlumnoUpdateView(UpdateView):
    model = alumnoTable
    form_class = AlumnoForm
    template_name = 'alumno/editar_alumno.html'
    success_url = reverse_lazy('index')

class AlumnoDeleteView(DeleteView):
    model = alumnoTable
    template_name = 'alumno/confirmar_eliminar.html'
    success_url = reverse_lazy('index')

def pagina_exito(request):
    return render(request, 'alumno/pagina_exito.html')
