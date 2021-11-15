from django import forms
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
        fields = ['Rut', 'Nombre', 'FechaIngreso', 'Correo', 'Imagen', 'IdSubGerencia', 'IdPerfil']
        labels = {
            'Rut': 'Rut del empleado',
            'Nombre': 'Nombre',
            'FechaIngreso': 'Fecha de ingreso',
            'Correo': 'Correo',
            'Imagen': 'Foto para perfil',
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
            'Correo': forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese correo',
                }
            ),
            'Imagen': forms.FileInput(
                attrs = {
                    'class':'form-control',
                }
            ),
            'IdSubGerencia': forms.Select(
                attrs = {
                    'class':'form-select'
                }
            ),
            'IdPerfil': forms.Select(
                attrs = {
                    'class':'form-select'
                }
            ),
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
            'NombreEvaluador': forms.TextInput(),
            'NombreCalibrador': forms.TextInput(),
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
            'IdPerfil': forms.Select(
                attrs = {
                    'class':'form-select'
                }
            ),
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
            'IdPerfil': forms.Select(
                attrs = {
                    'class':'form-select'
                }
            ),
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
            'IdCompetencia': forms.Select(
                attrs = {
                    'class':'form-select'
                }
            )
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
            'IdArea': forms.Select(
                attrs = {
                    'class':'form-select' 
                }
            )
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
            'IdGerencia': forms.Select(
                attrs = {
                    'class':'form-select'
                }
            )
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
class DetalleEvaluacionForm(forms.ModelForm):
    class Meta:
        model = DetalleEv
        fields = ['ComentarioEvaluador', 'Calificacion', 'AutoEvaluacion']
        labels = {
            'ComentarioEvaluador': 'Observacion',
            'Calificacion' : 'Calificacion',
            'AutoEvaluacion' : 'AutoEvaluacion'
        }
        widgets = { 
            'ComentarioEvaluador': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una observacion',
                }
            ),
            'Calificacion': forms.TextInput(),
            'AutoEvaluacion': forms.TextInput(),
        }


class EvaluacionForm(forms.ModelForm):

    class Meta:
        model = Evaluacion
        fields =['Estado', 'Fase', 'ComentarioCalibrador', 'IdEmpleado']
