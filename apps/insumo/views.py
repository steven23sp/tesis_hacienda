from django.urls import reverse_lazy

from apps.insumo.form import insumoForm
from apps.insumo.models import insumo
from django.views.generic import *


# Create your views here.
class insumo_list(ListView):
    model = insumo
    template_name = 'insumo/insumo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Insumo'
        context['nuevo'] = reverse_lazy('insumo:crear')
        context['url'] = reverse_lazy('insumo:lista')
        context['entidad'] = 'Insumo'
        return context


class insumo_create(CreateView):
    model = insumo
    form_class = insumoForm
    template_name = 'insumo/insumo_form.html'
    success_url = reverse_lazy('insumo:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Insumo'
        context['url'] = reverse_lazy('insumo:lista')
        context['entidad'] = 'Insumo'
        return context


class insumo_update(UpdateView):
    model = insumo
    form_class = insumoForm
    template_name = 'insumo/insumo_form.html'
    success_url = reverse_lazy('insumo:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Insumo'
        context['url'] = reverse_lazy('insumo:lista')
        context['entidad'] = 'Insumo'
        return context


class insumo_delete(DeleteView):
    model = insumo
    form_class = insumoForm
    template_name = '../../../sistema_yamaha/templates/prueba/form_delete.html'
    success_url = reverse_lazy('insumo:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Insumo'
        context['entidad'] = 'Insumo'

        return context
