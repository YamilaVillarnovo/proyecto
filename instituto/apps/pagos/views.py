from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.pagos.models import Pagos
from apps.pagos.forms import PagosForm
from django.urls import reverse_lazy

class PagoListView(ListView):
    model = Pagos
    template_name = 'pagos/index_pagos.html'
    context_object_name = 'pagos'

class PagoCreateView(CreateView):
    model = Pagos
    form_class = PagosForm
    template_name = 'pagos/carga_pagos.html'
    success_url = reverse_lazy('index_pagos')

class PagoUpdateView(UpdateView):
    model = Pagos
    form_class = PagosForm
    template_name = 'pagos/editar_pagos.html'
    success_url = reverse_lazy('index_pagos')

class PagoDeleteView(DeleteView):
    model = Pagos
    template_name = 'pagos/confirmar_eliminar_pagos.html'
    success_url = reverse_lazy('index_pagos')

def pagina_exito(request):
    return render(request, 'alumno/pagina_exito.html')
