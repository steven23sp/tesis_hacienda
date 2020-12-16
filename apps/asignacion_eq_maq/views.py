from django.urls import reverse_lazy

from apps.asignacion_eq_maq.form import asig_eq_maqForm
from apps.asignacion_eq_maq.models import asig_eq_maq
from django.views.generic import *


# Create your views here.
class asig_eq_maq_list(ListView):
    model = asig_eq_maq
    template_name = 'asignacion_equipo_maq/asi_eq_maq_list.html'
    #template_name = 'base2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Asignaciones de Maquinas y Equipos'
        context['nuevo'] = reverse_lazy('asignacion_ep_maq:crear')
        context['url'] = reverse_lazy('asignacion_ep_maq:lista')
        context['entidad'] = 'Asignacion Equipo y Maquinaria'
        return context


class asig_eq_maq_create(CreateView):
    model = asig_eq_maq
    form_class = asig_eq_maqForm
    template_name = 'asignacion_equipo_maq/asi_eq_maq_form.html'
    success_url = reverse_lazy('asignacion_ep_maq:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Asignacion'
        context['url'] = reverse_lazy('asignacion_ep_maq:lista')
        context['entidad'] = 'Asignacion Equipo y Maquinaria'
        return context

class asig_eq_maq_update(UpdateView):
    model = asig_eq_maq
    form_class = asig_eq_maqForm
    template_name = 'asignacion_equipo_maq/asi_eq_maq_form.html'
    success_url = reverse_lazy('asignacion_ep_maq:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Asignacion'
        context['url'] = reverse_lazy('asignacion_ep_maq:lista')
        context['entidad'] = 'Asignacion Equipo y Maquinaria'
        return context


class asig_eq_maq_delete(DeleteView):
    model = asig_eq_maq
    form_class = asig_eq_maqForm
    template_name = '../../../sistema_yamaha/templates/prueba/form_delete.html'
    success_url = reverse_lazy('asignacion_ep_maq:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Asignacion'
        context['entidad'] = 'Asignacion Equipo y Maquinaria'

        return context
