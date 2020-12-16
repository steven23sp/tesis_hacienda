from django.urls import reverse_lazy

from apps.labor.form import laborForm
from apps.labor.models import labor
from django.views.generic import *


# Create your views here.
class labor_list(ListView):
    model = labor
    template_name = 'labor/labor_list.html'
    #template_name = 'base2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Labores'
        context['nuevo'] = reverse_lazy('labor:crear')
        context['url'] = reverse_lazy('labor:lista')
        context['entidad'] = 'Labor'
        return context


class labor_create(CreateView):
    model = labor
    form_class = laborForm
    template_name = 'labor/labor_form.html'
    success_url = reverse_lazy('labor:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Labor'
        context['url'] = reverse_lazy('labor:lista')
        context['entidad'] = 'Labor'
        return context

class labor_update(UpdateView):
    model = labor
    form_class = laborForm
    template_name = 'labor/labor_form.html'
    success_url = reverse_lazy('labor:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Labor'
        context['url'] = reverse_lazy('labor:lista')
        context['entidad'] = 'Labor'
        return context


class labor_delete(DeleteView):
    model = labor
    form_class = laborForm
    template_name = '../../../sistema_yamaha/templates/prueba/form_delete.html'
    success_url = reverse_lazy('labor:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Labor'
        context['entidad'] = 'Labor'

        return context

