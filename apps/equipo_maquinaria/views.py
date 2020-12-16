from django.urls import reverse_lazy

from apps.equipo_maquinaria.form import equipo_maquiForm
from apps.equipo_maquinaria.models import equipo_maquinaria
from django.views.generic import *


# Create your views here.
class equi_maq_list(ListView):
    model = equipo_maquinaria
    template_name = 'equipo_maquinaria/equi_maq_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de equipo y maquinaria'
        context['nuevo'] = reverse_lazy('equipo_maquinaria:crear_equipo_maquinaria')
        context['url'] = reverse_lazy('empleado:lista_empleado')
        context['entidad'] = 'Equipo y Maquinaria'
        return context


class equi_maq_create(CreateView):
    model = equipo_maquinaria
    form_class = equipo_maquiForm
    template_name = 'equipo_maquinaria/equi_maq_form.html'
    success_url = reverse_lazy('equipo_maquinaria:lista_equipo_maquinaria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Equipo y Maquinaria'
        context['url'] = reverse_lazy('equipo_maquinaria:lista_equipo_maquinaria')
        context['entidad'] = 'Equipo y Maquinaria'
        return context


class equi_maq_update(UpdateView):
    model = equipo_maquinaria
    form_class = equipo_maquiForm
    template_name = 'equipo_maquinaria/equi_maq_form.html'
    success_url = reverse_lazy('equipo_maquinaria:lista_equipo_maquinaria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Equipo y Maquinaria'
        context['url'] = reverse_lazy('equipo_maquinaria:lista_equipo_maquinaria')
        context['entidad'] = 'Equipo y Maquinaria'
        return context


class equi_maq_delete(DeleteView):
    model = equipo_maquinaria
    form_class = equipo_maquiForm
    template_name = '../../../sistema_yamaha/templates/prueba/form_delete.html'
    success_url = reverse_lazy('equipo_maquinaria:lista_equipo_maquinaria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Equipo y Maquinaria'
        context['entidad'] = 'Empleado'
        context['url'] = reverse_lazy('equipo_maquinaria:lista_equipo_maquinaria')

        return context
