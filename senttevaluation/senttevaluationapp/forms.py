
from django import forms
from .models import EMPLEADO

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = EMPLEADO()
        fields = '__all__'