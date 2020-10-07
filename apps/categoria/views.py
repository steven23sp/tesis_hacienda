from django.urls import reverse_lazy
from django.views.generic import *
from apps.categoria.models import *
from apps.categoria.form import categoriaForm


# Create your views here.

class categoria_list(ListView):
    model = categoria
    template_name = 'categoria/categoria_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorias'
        context['nuevo'] = reverse_lazy('categoria:crear')
        context['url'] = reverse_lazy('categoria:lista')
        context['entidad'] = 'Categoria'
        return context


class categoria_create(CreateView):
    model = categoria
    form_class = categoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Categoria'
        context['url'] = reverse_lazy('categoria:lista')
        context['entidad'] = 'Categoria'

        return context


class categoria_update(UpdateView):
    model = categoria
    form_class = categoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Categoria'
        context['url'] = reverse_lazy('categoria:lista')
        context['entidad'] = 'Categoria'
        return context


class categoria_delete(DeleteView):
    model = categoria
    form_class = categoriaForm
    template_name = 'prueba/form_delete.html'
    success_url = reverse_lazy('categoria:lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de Categoria'
        context['entidad'] = 'Categoria'

        return context
