from django import forms
from django.db.models.base import ModelBase
from django.forms import fields
from django.forms.models import model_to_dict
from .models import AccionClave, Competencia, DetalleEv, Empleado, Cargo, Gerencia, PerfilRol, SubGerencia
from .models import AccionClave, Competencia, Empleado, Cargo, Gerencia, PerfilRol, SubGerencia


class LoginForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['Rut','Password']
        labels = {
            'Rut': 'Rut',
            'Password': 'Contraseña',
        }
        widgets = {
            'Rut': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese rut',
                }
            ),
            'Password': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese contraseña',
                }
            ),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['Rut','Nombre','FechaIngreso','Password','Correo','IdSubGerencia']
        labels = {
            'Rut': 'Rut del empleado',
            'Nombre': 'Nombre',
            'FechaIngreso': 'Fecha de ingreso',
            'Password': 'Contraseña',
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
            'IdSubGerencia': forms.Select(
            ),
            
        }
      
class PerfilRolForm(forms.ModelForm):
    class Meta:
        model = PerfilRol
        fields = ['Rol','RelacionEvaluado','NombreEvaluador','NombreCalibrador']
        labels = {
            'Rol': 'Rol',
            'RelacionEvaluado': 'Relacion con el evaluado',
            'NombreEvaluador': 'Nombre del evaluador',
            'NombreCalibrador': 'Nombredel calibrador',
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
                    'placeholder': 'Ingrese el nombre del evaluador',
                }
            ),
            'NombreCalibrador': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre del calibrador',
                }
            )            
        }

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['NombreCargo']
        labels = {
            'NombreCargo': 'Nombre Cargo',
        }
        widgets = {
            'NombreCargo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre del cargo',
                }
            )
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