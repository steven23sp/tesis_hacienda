from django import forms
from datetime import *
from django.forms import SelectDateWidget, TextInput, NumberInput, EmailInput
from .models import asig_eq_maq
from tempus_dominus.widgets import DatePicker


class asig_eq_maqForm(forms.ModelForm):
    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        this_year = datetime.now().year
        years = range(this_year - 15, this_year - 3)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['fecha_asig'].widget = DatePicker()
            self.fields['observacion'].widget = TextInput(
                attrs={'placeholder': 'Ingrese su direccion con maximo 50 caracteres',
                       'class': 'form-control form-rounded', 'autocomplete': 'off'})

        # habilitar, desabilitar, y mas

    class Meta:
        model = asig_eq_maq
        fields = ['fecha_asig',
                  'empleado',
                  'equipo_maquinaria',
                  'observacion'
                  ]
        labels = {
            'fecha_asig': 'Fecha de asignacion',
            'empleado': 'Responsable',
            'equipo_maquinaria': 'Tipo',
            'observacion': 'Observacion'

        }
        widgets = {
            'fecha_asig': forms.DateInput(),
            'empleado': forms.Select(attrs={'class': 'selectpicker', 'data-width': 'fit'}),
            'equipo_maquinaria': forms.Select(attrs={'class': 'selectpiker', 'date-width': 'fit'}),
            'observacion': forms.Textarea(),
        }
