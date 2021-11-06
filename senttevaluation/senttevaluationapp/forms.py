from django import forms
from django.forms import widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['Rut', 'Nombre', 'FechaIngreso', 'Correo', 'IdSubGerencia', 'IdPerfil']
        labels = {
            'Rut': 'Rut del empleado',
            'Nombre': 'Nombre',
            'FechaIngreso': 'Fecha de ingreso',
            'Correo': 'Correo',
            'IdSubGerencia': 'Subgerencia',
            'IdPerfil': 'Perfil',
        }
        widgets = {
            'Rut': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese rut',
                }
            ),
            'Nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre y apellidos',
                }
            ),
            'FechaIngreso': forms.TextInput(
                attrs = {
                    'type': 'date',
                }
            ),
            'Correo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese correo',
                }
            ),
            'IdSubGerencia': forms.Select(),
            'IdPerfil': forms.Select(),
        }

class PerilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        labels = {
            'NombrePerfil': 'Nombre Perfil'
        }
      
class PerfilRolForm(forms.ModelForm):
    class Meta:
        model = PerfilRol
        fields = ['Rol', 'RelacionEvaluado', 'NombreEvaluador', 'NombreCalibrador']
        labels = {
            'Rol': 'Rol',
            'RelacionEvaluado': 'Relacion con el evaluado',
            'NombreEvaluador': 'Nombre del evaluador',
            'NombreCalibrador': 'Nombre del calibrador',
        }
        widgets = {
            'Rol': forms.Select(
                choices = {
                    (1, "Evaluador"),
                    (2, "Evaluado"),
                    (3, "Calibrador"),
                }
            ),
            'RelacionEvaluado': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese la relación',
                }
            ),
            'NombreEvaluador': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese nombre Evaluador'
                }
            ),
            'NombreCalibrador': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese nombre Calibrador'
                }
            ),
        }

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['NombreCargo', 'IdPerfil']
        labels = {
            'NombreCargo': 'Nombre Cargo',
            'IdPerfil': 'Perfil',
        }
        widgets = {
            'NombreCargo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre del cargo',
                }
            ),
            'IdPerfil': forms.Select(),
        }

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['NombreCompetencia', 'Definicion', 'IdPerfil']
        labels = {
            'NombreCompetencia': 'Nombre competencia',
            'Definicion': 'Definicion',
            'IdPerfil': 'Perfil',
        }
        widgets = {
            'NombreCompetencia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre de la competencia',
                }
            ),
            'Definicion': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese definición',
                }
            ),
            'IdPerfil': forms.Select(),
        }

class AccionesForm(forms.ModelForm):
    class Meta:
        model = AccionClave        
        fields = ['Descripcion', 'IdCompetencia']
        labels = {
            'Descripcion': 'Descripción',
            'IdCompetencia': 'Competencia',
        }
        widgets = {
            'Descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese descripción',
                }
            ),
            'IdCompetencia': forms.Select()
        }

class GerenciaForm(forms.ModelForm):
    class Meta:
        model = Gerencia
        fields = ['NombreGerencia']
        labels = {
            'NombreGerencia': 'Nombre gerencia'            
        }
        widgets = {
            'NombreGerencia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre de la gerencia',
                }
            ),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model=Perfil
        fields = ['NombrePerfil']
        labels = {
            'NombrePerfil': 'Nombre Perfil'
        }
        widgets = {
            'NombrePerfil': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder':'Ingrese nombre del prefil'
                }
            )
        }

class AreaFrom(forms.ModelForm):
    class Meta:
        model=Area
        fields = ['NombreArea', 'IdGerencia']
        labels = {
            'NombreArea':'Nombre Area',
            'IdGerencia':'Gerencia'
        }
        widgets = {
            'NombreArea': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese nombre del area',
                }
            ),
            'IdArea': forms.Select()
        }

class SubgerenciaForm(forms.ModelForm):
    class Meta:
        model = SubGerencia
        fields = ['NombreSubgerencia', 'IdGerencia']
        labels = {
            'NombreSubgerencia': 'Nombre subgerencia',
            'IdGerencia': 'Gerencia',
        }
        widgets = {
            'NombreSubgerencia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre de la subgerencia',
                }
            ),
            'IdGerencia': forms.Select()
        }


class PlanAccionForm(forms.ModelForm):

    class Meta:
        model = PlanAccion
        fields = ['Accion', 'Medicion']
        labels = {
            'Accion': 'Accion',
            'Medicion': 'Medicion'
        }
        widgets = {
            'Accion': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una accion',
                }
            ),
            'Medicion': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una medicion',
                }
            )
        }
class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = DetalleEv
        fields = '__all__'