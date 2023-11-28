from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.reservas.models import Reservas
from apps.reservas.forms import ReservasForm
from django.urls import reverse_lazy

class ReservaListView(ListView):
    model = Reservas
    template_name = 'reservas/index_reserva.html'
    context_object_name = 'reservas'

class ReservaCreateView(CreateView):
    model = Reservas
    form_class = ReservasForm
    template_name = 'reservas/cargar_reserva.html'
    success_url = reverse_lazy('index_reserva')

class ReservaUpdateView(UpdateView):
    model = Reservas
    form_class = ReservasForm
    template_name = 'reservas/editar_reserva.html'
    success_url = reverse_lazy('index_reserva')

class ReservaDeleteView(DeleteView):
    model = Reservas
    template_name = 'reservas/confirmar_eliminar_reserva.html'
    success_url = reverse_lazy('index_reserva')
