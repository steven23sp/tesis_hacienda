from django import forms
from datetime import *
from django.forms import SelectDateWidget, TextInput, NumberInput, EmailInput, Select

from .models import insumo


class insumoForm(forms.ModelForm):
    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        this_year = datetime.now().year
        years = range(this_year - 15, this_year - 3)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

            self.fields['nombre'].widget = TextInput(
                attrs={'placeholder': 'Ingrese el nombre del insumo', 'class': 'form-control', 'autofocus': True})
            self.fields['descripcion'].widget = TextInput(
                attrs={'placeholder': 'Ingrese una descripcion', 'class': 'form-control form-rounded'})
            self.fields['categoria'].widget.attrs = {
                'class': 'form-control select2',
                'data-live-search': 'true'}
            self.fields['presentacion'].widget.attrs = {
                'class': 'form-control select2',
            }
            self.fields['pvp'].widget.attrs = {
                'class': 'form-control form-control-sm input-sm',
            }
        # form - control
        # form - control - sm
        # input - sm
        # habilitar, desabilitar, y mas

    class Meta:
        model = insumo
        fields = ['nombre',
                  'categoria',
                  'presentacion',
                  'pvp',
                  'descripcion'
                  ]
        labels = {
            'nombre': 'Nombre',
            'categoria': 'Categoria',
            'presentacion': 'Presentacion',
            'pvp': 'P.V.P.',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'nombre': forms.TextInput(),
            'categoria': forms.Select(),
            'pvp': forms.TextInput(),
            'descripcion': forms.TextInput(),
        }
