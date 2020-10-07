from django.urls import reverse_lazy

from apps.asistencia.form import asistenciaForm
from apps.asistencia.models import asistencia
from django.views.generic import *


# Create your views here.
class asientencia_list(ListView):
    model = asistencia
    template_name = 'asistencias/asistencia_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Asitencias'
        context['nuevo'] = reverse_lazy('asistencia:crear')
        context['url'] = reverse_lazy('asistencia:lista')
        context['entidad'] = 'Asistencia'
        return context


class asistencia_create(CreateView):
    model = asistencia
    form_class = asistenciaForm
    template_name = 'asistencias/asistencia_form.html'
    success_url = reverse_lazy('asistencia:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Asistencias'
        context['url'] = reverse_lazy('asistencia:lista')
        context['entidad'] = 'Asistencias'
        return context
