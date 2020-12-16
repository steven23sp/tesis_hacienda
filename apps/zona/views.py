from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from apps.zona.form import zonaForm
from apps.zona.models import zona
from django.views.generic import *


# Create your views here.
class zona_list(ListView):
    model = zona
    template_name = 'zona/zona_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Zonas'
        context['nuevo'] = reverse_lazy('zona:crear')
        context['url'] = reverse_lazy('zona:lista')
        context['entidad'] = 'Zonas'
        return context


class zona_create(CreateView):
    model = zona
    form_class = zonaForm
    template_name = 'zona/zona_form.html'
    success_url = reverse_lazy('zona:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Zonas'
        context['url'] = reverse_lazy('zona:lista')
        context['entidad'] = 'Zonas'
        return context


class zona_update(UpdateView):
    model = zona
    form_class = zonaForm
    template_name = 'zona/zona_form.html'
    success_url = reverse_lazy('zona:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Zonas'
        context['url'] = reverse_lazy('zona:lista')
        context['entidad'] = 'Zonas'
        return context


class zona_delete(DeleteView):
    model = zona
    form_class = zonaForm
    template_name = '../../../sistema_yamaha/templates/prueba/form_delete.html'
    success_url = reverse_lazy('zona:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Zonas'
        context['url'] = reverse_lazy('zona:lista')
        context['entidad'] = 'Zonas'

        return context

@csrf_exempt
def estado(request):
    data = {}
    try:
        id = int(request.POST['id'])
        print(id)
        ps = zona.objects.get(pk=id)
        if ps.estado == 1:
            ps.estado = 0
            ps.save()
            data['resp'] = True
        elif ps.estado == 0:
            ps.estado = 1
            ps.save()
            data['resp'] = True
        else:
            data['error'] = 'Ha ocurrido un error'
    except Exception as e:
        data['error'] = str(e)
    return JsonResponse(data)

