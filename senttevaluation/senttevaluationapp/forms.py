from django import forms
from django.db.models.base import ModelBase
from django.forms.models import model_to_dict
from django.forms.widgets import Select
from .models import AccionClave, Competencia, DetalleEv, Empleado, Cargo, Gerencia, Perfil, PerfilRol, SubGerencia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_text = {k:"" for k in fields}
        labels = {
            'username': 'Usuario',
        }
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['Rut','Nombre','FechaIngreso','Correo','IdSubGerencia']
        labels = {
            'Rut': 'Rut del empleado',
            'Nombre': 'Nombre',
            'FechaIngreso': 'Fecha de ingreso',
            'Correo': 'Correo',
            'IdSubGerencia': 'Subgerencia',
            
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
            'FechaIngreso': forms.SelectDateWidget(
            ),
            'Password': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese contraseña',
                }
            ),
            'Correo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese correo',
                }
            ),
            
            'IdSubGerencia': forms.Select(),
            
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
        fields = ['Rol','RelacionEvaluado','IdEvaluador','IdCalibrador']
        labels = {
            'Rol': 'Rol',
            'RelacionEvaluado': 'Relacion con el evaluado',
            'IdEvaluador': 'Nombre del evaluador',
            'IdCalibrador': 'Nombre del calibrador',
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
            'IdEvaluador': forms.Select(),
            'IdCalibrador': forms.Select(),
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
        fields = ['NombreCompetencia','Definicion','IdPerfil']
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
            'IdPerfil': forms.Select()
        }

class AccionesForm(forms.ModelForm):
    class Meta:
        model = AccionClave        
        fields = ['Descripcion','IdCompetencia']
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
        fields = ['NombreGerencia','IdArea']
        labels = {
            'NombreGerencia': 'Nombre gerencia',
            'IdArea': 'Area',
        }
        widgets = {
            'NombreGerencia': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre de la gerencia',
                }
            ),
            'IdArea': forms.Select()
        }

class SubgerenciaForm(forms.ModelForm):
    class Meta:
        model = SubGerencia
        fields = ['NombreSubgerencia','IdGerencia']
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

class EvaluacionForm(forms.ModelForm):

    class Meta:
        model = DetalleEv
        fields = '__all__'