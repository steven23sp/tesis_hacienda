from django.urls import reverse_lazy

from apps.proveedor.form import proveedorForm
from apps.proveedor.models import proveedor
from django.views.generic import *


# Create your views here.
class proveedor_list(ListView):
    model = proveedor
    template_name = 'proveedor/proveedor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proveedor'
        context['nuevo'] = reverse_lazy('proveedor:crear')
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedor'
        return context


class proveedor_create(CreateView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Proveedor'
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedor'
        return context


class proveedor_update(UpdateView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Proveedor'
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedor'
        return context


class proveedor_delete(DeleteView):
    model = proveedor
    form_class = proveedorForm
    template_name = 'prueba/form_delete.html'
    success_url = reverse_lazy('proveedor:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Proveedor'
        context['url'] = reverse_lazy('proveedor:lista')
        context['entidad'] = 'Proveedor'

        return context
