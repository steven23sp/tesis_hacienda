from django.urls import reverse_lazy

from apps.cliente.form import clienteForm
from apps.cliente.models import cliente
from django.views.generic import *


# Create your views here.
class cliente_list(ListView):
    model = cliente
    template_name = 'cliente/cliente_list.html'
    #template_name = 'base2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['nuevo'] = reverse_lazy('cliente:crear')
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        return context


class cliente_create(CreateView):
    model = cliente
    form_class = clienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Cliente'
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        return context

class cliente_update(UpdateView):
    model = cliente
    form_class = clienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Cliente'
        context['url'] = reverse_lazy('cliente:lista')
        context['entidad'] = 'Cliente'
        return context


class cliente_delete(DeleteView):
    model = cliente
    form_class = clienteForm
    template_name = 'prueba/form_delete.html'
    success_url = reverse_lazy('cliente:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Cliente'
        context['entidad'] = 'Cliente'

        return context
