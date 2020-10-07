from django.urls import reverse_lazy

from apps.empleado.form import empleadoForm
from apps.empleado.models import empleado
from django.views.generic import *


# Create your views here.
class emple_list(ListView):
    model = empleado
    template_name = 'empleado/empleado_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de empleados'
        context['nuevo'] = reverse_lazy('empleado:crear_empleado')
        context['url'] = reverse_lazy('empleado:lista_empleado')
        context['entidad'] = 'Empleado'
        return context


class empleadao_create(CreateView):
    model = empleado
    form_class = empleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado:lista_empleado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Empleados'
        context['url'] = reverse_lazy('empleado:lista_empleado')
        context['entidad'] = 'Empleado'
        return context


class empleadao_update(UpdateView):
    model = empleado
    form_class = empleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('empleado:lista_empleado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Empleados'
        context['url'] = reverse_lazy('empleado:lista_empleado')
        context['entidad'] = 'Empleado'
        return context


class empleadao_delete(DeleteView):
    model = empleado
    form_class = empleadoForm
    template_name = 'prueba/form_delete.html'
    success_url = reverse_lazy('empleado:lista_empleado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Empleado'
        context['entidad'] = 'Empleado'

        return context
