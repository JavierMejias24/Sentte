from django import forms
from django.forms import widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username':'Usuario',
            'password1':'Contraseña',
            'password2':'Confirmar contraseña',
        }
        help_texts = { 
            'username': ('Debe ser único, no puede estar en blanco'),
            'password': ('No puede estar en blanco'),
            'password2': ('Debe ser igual a la contraseña, no puede estar en blanco'),
        }
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Nombre de usuario',
                }
            ),
            'password1': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Contraseña',
                }
            ),
            'password2': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Repita contraseña',
                }
            ),
        }

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
        help_texts = { 
            'Rut': ('Entre 11 y 12 caracteres, no puede estar en blanco'),
            'Nombre': ('No puede estar en blanco'),
            'FechaIngreso': ('No puede estar en blanco'),
            'Correo': ('No puede estar en blanco, debe incluir @'),
            'Imagen': ('Puede estar en blanco'),
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
            'RelacionEvaluado': 'Relación con el evaluado',
            'NombreEvaluador': 'Nombre del evaluador',
            'NombreCalibrador': 'Nombre del calibrador',
        }
        help_texts = {
            'RelacionEvaluado': ('Puede estar en blanco'),
            'NombreEvaluador': ('Puede estar en blanco'),
            'NombreCalibrador': ('Puede estar en blanco'),
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
                    'placeholder': 'Jefe directo...',
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
            'NombreCargo': 'Nombre cargo',
            'IdPerfil': 'Perfil',
        }
        help_texts = { 
            'NombreCargo': ('No puede estar en blanco'),
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
            'Definicion': 'Definición',
            'IdPerfil': 'Perfil',
        }
        help_texts = { 
            'NombreCompetencia': ('No puede estar en blanco'),
            'Definicion': ('No puede estar en blanco'),
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
        help_texts = { 
            'Descripcion': ('No puede estar en blanco'),
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
        help_texts = { 
            'NombreGerencia': ('No puede estar en blanco'),
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
        help_texts = { 
            'NombrePerfil': ('No puede estar en blanco'),
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
            'NombreArea':'Nombre área',
            'IdGerencia':'Gerencia'
        }
        help_texts = { 
            'NombreArea': ('No puede estar en blanco'),
        }
        widgets = {
            'NombreArea': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese nombre del area',
                }
            ),
            'IdGerencia': forms.Select(
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
        help_texts = { 
            'NombreSubgerencia': ('No puede estar en blanco'),
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
            'Accion': 'Acción',
            'Medicion': 'Medición'
        }
        widgets = {
            'Accion': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una acción',
                }
            ),
            'Medicion': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese una medición',
                }
            )
        }
class DetalleEvaluacionForm(forms.ModelForm):
    class Meta:
        model = DetalleEv
        fields = ['Calificacion']
        labels = {
            'Calificacion' : '',
        }
        widgets = {
            'Calificacion': forms.Select(
                attrs = {
                    'class':'form-select',
                }
            ),
        }

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['Estado', 'Fase', 'ComentarioCalibrador', 'IdEmpleado']

class RegistrosForm(forms.Form):
    select = [
        (1, 10),
        (2, 25),
        (3, 50),
        (4, 100),
    ]
    Select = forms.ChoiceField(initial=1, choices=select, label="Mostrar")
