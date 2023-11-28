from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.horarios.models import Horarios
from apps.horarios.forms import HorariosForm
from django.urls import reverse_lazy

class HorarioListView(ListView):
    model = Horarios
    template_name = 'horarios/index_horarios.html'
    context_object_name = 'horarios'

class HorarioCreateView(CreateView):
    model = Horarios
    form_class = HorariosForm
    template_name = 'horarios/cargar_horario.html'
    success_url = reverse_lazy('index_horarios')

class HorarioUpdateView(UpdateView):
    model = Horarios
    form_class = HorariosForm
    template_name = 'horarios/editar_horario.html'
    success_url = reverse_lazy('index_horarios')

class HorarioDeleteView(DeleteView):
    model = Horarios
    template_name = 'horarios/confirmar_eliminar_horario.html'
    success_url = reverse_lazy('index_horarios')

def pagina_exito(request):
    return render(request, 'alumno/pagina_exito.html')