from django import forms
from datetime import *
from django.forms import SelectDateWidget, TextInput, NumberInput, EmailInput
from .models import asistencia
from tempus_dominus.widgets import DatePicker

class asistenciaForm(forms.ModelForm):
    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        this_year = datetime.now().year
        years = range(this_year - 15, this_year - 3)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['fecha'].widget = DatePicker(
                attrs={'class':'form-control datetimepicker-input','autocomplete': 'off'})


        # habilitar, desabilitar, y mas

    class Meta:
        model = asistencia
        fields = ['fecha',
                  'estado',
                  'empleado'
                  ]
        labels = {
            'fecha': 'Fecha de Asistencia',
            'estado': 'Estado',
            'empleado': 'Empleado'

        }
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'form-control datetimepicker-input'}),
            'estado': forms.Select(attrs={'class': 'selectpicker', 'data-width': 'fit'}),
            'empleado': forms.Select()
        }
