from re import I
from django.db import models
from django.db.models import query
from django.db.models.deletion import CASCADE, PROTECT
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import User
from django.db.models.expressions import Case
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields.related import ForeignKey
from django.forms.widgets import NullBooleanSelect


# Create your models here.

class Area(models.Model):
    NombreArea = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])

    def __str__(self):
        return self.NombreArea

class Gerencia(models.Model):
    NombreGerencia = models.CharField(max_length=50, unique=True ,validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    IdArea = models.ForeignKey(Area, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.NombreGerencia

class SubGerencia(models.Model):
    NombreSubgerencia = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    IdGerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.NombreSubgerencia
    
class Perfil(models.Model):
    NombrePerfil = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    def __str__(self):
        return self.NombrePerfil
        
class Cargo(models.Model):
    NombreCargo = models.CharField(max_length=50, unique=True ,validators=[RegexValidator(regex=r'^[a-zA-Z]')])
    IdPerfil = models.ForeignKey(Perfil, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.NombreCargo
class Empleado(models.Model):
    Rut = models.CharField(max_length=12, unique=True, validators=[RegexValidator(regex=r'^(\d{1,3}(?:.\d{1,3}){2}-[\dkK])$' )])
    Nombre = models.CharField(max_length=100, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    FechaIngreso = models.DateField()
    Correo = models.CharField(max_length=100, unique=True, validators=[EmailValidator])
    IdPerfil = models.ForeignKey(Perfil, on_delete=CASCADE, default=1)
    user = models.OneToOneField(User, on_delete=CASCADE)
    IdSubGerencia = models.ForeignKey(SubGerencia, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.Nombre 

class PerfilRol(models.Model):
    Roles = [
        (1, "Evaluador"),
        (2, "Evaluado"),
        (3, "Calibrador"),
    ]
    Rol = models.IntegerField(choices=Roles, default=1)
    RelacionEvaluado = models.CharField(max_length=50, blank=True, default='',validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    NombreEvaluador = models.CharField(max_length=100, null=True, blank=True, default='')
    NombreCalibrador = models.CharField(max_length=100, null=True, blank=True, default='')
    IdEmpleado = models.ForeignKey(Empleado, on_delete=CASCADE)

    def __str__(self):
        return self.get_Rol_display()

class Evaluacion(models.Model):
    Estado = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    Fase = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    ComentarioCalibrador = models.CharField(max_length=80, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    IdEmpleado = models.ForeignKey(Empleado, on_delete=CASCADE, default=1)

class PlanAccion(models.Model):
    Accion = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    Medicion = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])

class DetalleEv(models.Model):
    FechaEvaluacion = models.DateField()
    ComentarioEvaluador = models.CharField(max_length=100, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    Calificacion = models.IntegerField(validators=[RegexValidator(regex=r'^[0-9]')])
    AutoEvaluacion = models.IntegerField(validators=[RegexValidator(regex=r'^[0-9]')])
    IdEvaluacion = models.ForeignKey(Evaluacion, on_delete=CASCADE, default=1)
    IdPlanAccion = models.ForeignKey(PlanAccion, on_delete=CASCADE, default=1)

class Competencia(models.Model):
    NombreCompetencia = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    Definicion = models.CharField(max_length=1000, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    IdPerfil = models.ForeignKey(Perfil, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.NombreCompetencia

class AccionClave(models.Model):
    Descripcion = models.CharField(max_length=1000, unique=True, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    IdCompetencia = models.ForeignKey(Competencia, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.Descripcion

class EmpleadoEliminado(models.Model):
    Rut = models.CharField(max_length=12)
    Nombre = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)
    Rol = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    FechaEliminacion = models.DateField(auto_now=True)