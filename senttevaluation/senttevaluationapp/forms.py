
from django import forms
from django.db.models.base import ModelBase
from django.forms import fields
from django.forms.models import model_to_dict
from .models import AccionClave, Competencia, Empleado, Cargo, Gerencia, PerfilRol, SubGerencia

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'
      
class PerfilRolForm(forms.ModelForm):
    class Meta:
        model = PerfilRol
        fields = '__all__'

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

class AccionesForm(forms.ModelForm):
    class Meta:
        model = AccionClave
        fields = '__all__'

class GerenciaForm(forms.ModelForm):
    class Meta:
        model = Gerencia
        fields = '__all__'

class SubgerenciaForm(forms.ModelForm):
    class Meta:
        model = SubGerencia
        fields = '__all__'