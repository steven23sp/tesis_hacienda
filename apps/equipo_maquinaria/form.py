from django import forms
from datetime import *
from django.forms import SelectDateWidget, TextInput, NumberInput, EmailInput
from tempus_dominus.widgets import *
from .models import equipo_maquinaria
class equipo_maquiForm(forms.ModelForm):
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
                attrs={'placeholder': 'Ingrese el nombre de la maquina o equipo', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['descripcion'].widget = TextInput(
                attrs={'placeholder': 'Ingrese una breve descripcion', 'class': 'form-control form-rounded','autocomplete': 'off'})
            self.fields['fecha_registro'].widget = DatePicker(
                attrs={'placeholder': 'Ingrese su direccion con maximo 50 caracteres', 'class': 'form-control form-rounded','autocomplete': 'off'})

        # habilitar, desabilitar, y mas

    class Meta:
        model = equipo_maquinaria
        fields = ['nombre',
                  'tipo',
                  'descripcion',
                  'fecha_registro'
                  ]
        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'descripcion': 'Descripcion',
            'fecha_registro': 'Fecha de registro'

        }
        widgets = {
            'nombre': forms.TextInput(),
            'tipo': forms.Select(attrs={'class': 'selectpicker', 'data-width': 'fit'}),
            'descripcion': forms.TextInput(),
            'fecha_registro': forms.DateInput()
        }
