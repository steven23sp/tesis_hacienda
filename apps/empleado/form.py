from django import forms
from datetime import *
from django.forms import SelectDateWidget, TextInput, NumberInput, EmailInput
from .models import empleado
from tempus_dominus.widgets import DatePicker


class empleadoForm(forms.ModelForm):
    # constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        this_year = datetime.now().year
        years = range(this_year - 15, this_year - 3)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

            self.fields['nombres'].widget = TextInput(
                attrs={'placeholder': 'Ingrese sus dos nombres', 'class': 'form-control form-rounded','autocomplete':'off'})
            self.fields['apellidos'].widget = TextInput(
                attrs={'placeholder': 'Ingrese sus dos Apellidos', 'class': 'form-control form-rounded','autocomplete':'off'})
            self.fields['cedula'].widget = TextInput(
                attrs={'placeholder': 'Ingrese numero de cedula', 'class': 'form-control form-rounded','autocomplete':'off'})
            self.fields['edad'].widget = NumberInput(
                attrs={'placeholder': 'Ingrese su edad ', 'class': 'form-control form-rounded','autocomplete':'off'})
            self.fields['correo'].widget = EmailInput(
                attrs={'placeholder': 'abc@correo.com', 'class': 'form-control form-rounded','autocomplete':'off'})
            self.fields['telefono'].widget = TextInput(
                attrs={'placeholder': 'Ingrese numero de telefono', 'class': 'form-control form-rounded','autocomplete':'off'})

            self.fields["fecha_nac"].widget = DatePicker()

            self.fields['educ_primaria'].widget = TextInput(
                attrs={'placeholder': 'Educacion Primaria', 'class': 'form-control form-rounded'})
            self.fields['educ_secundaria'].widget = TextInput(
                attrs={'placeholder': 'Educacion Secundaria', 'class': 'form-control form-rounded'})
            self.fields['educ_superior'].widget = TextInput(
                attrs={'placeholder': 'Educacion Superior', 'class': 'form-control form-rounded'})
        # habilitar, desabilitar, y mas

    class Meta:
        model = empleado
        fields = ['nombres',
                  'apellidos',
                  'cedula',
                  'edad',
                  'correo',
                  'telefono',
                  'direccion',
                  'estado_civil',
                  'fecha_nac',
                  'estado',
                  'educ_primaria',
                  'educ_secundaria',
                  'educ_superior',

                  ]
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apelidos',
            'cedula': 'Cedula',
            'edad': 'Edad',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'estado_civil': ' Estado Civil',
            'fecha_nac': 'Fecha Nacimiento',
            'estado': 'Estado',
            'educ_primaria': 'Educacion Primaria',
            'educ_secundaria': 'Educacion Secundaria',
            'educ_superior': 'Educacion Superior',

        }
        widgets = {
            'nombres': forms.TextInput(
                attrs={'placeholder': 'Ingrese sus dos nombres', 'class': 'form-control form-rounded'}),
            'apellidos': forms.TextInput(
                attrs={'placeholder': 'Ingrese sus dos apellidos', 'class': 'form-control form-rounded'}),
            'cedula': forms.TextInput(
                attrs={'placeholder': 'Ingrese su numero de cedula', 'class': 'form-control form-rounded'}),
            'edad': forms.NumberInput(),
            'correo': forms.EmailInput(
                attrs={'placeholder': 'Ingrese sus dos correo', 'class': 'form-control form-rounded'}),
            'telefono': forms.TextInput(
                attrs={'placeholder': 'Ingrese sus dos telefono', 'class': 'form-control form-rounded'}),
            'direccion': forms.TextInput(
                attrs={'placeholder': 'Ingrese sus dos direccion', 'class': 'form-control form-rounded'}),
            'estado_civil': forms.Select(attrs={'class': 'selectpicker', 'data-width': 'fit'}),
            'fecha_nac': forms.DateTimeInput(format='%d-%m-%Y', attrs={'class': 'form-control''datetimepicker-input'}),
            'estado': forms.Select(attrs={'class': 'selectpicker', 'data-width': 'fit'}),
            'educ_primaria': forms.TextInput(
                attrs={'placeholder': 'Escuela Primaria', 'class': 'form-control form-rounded'}),
            'educ_secundaria': forms.TextInput(
                attrs={'placeholder': 'Escuela Secundaria', 'class': 'form-control form-rounded'}),
            'educ_superior': forms.TextInput(
                attrs={'placeholder': 'Educacion Superior', 'class': 'form-control form-rounded'})
        }
