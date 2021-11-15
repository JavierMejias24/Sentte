from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import User

# Create your models here.

class Gerencia(models.Model):
    NombreGerencia = models.CharField(max_length=50, unique=True ,validators=[RegexValidator(regex=r'^[a-zA-Z]')])

    def __str__(self):
        return self.NombreGerencia

class Area(models.Model):
    NombreArea = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    IdGerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.NombreArea

class SubGerencia(models.Model):
    NombreSubgerencia = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
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
    Rut = models.CharField(max_length=12, null=False, unique=True, validators=[RegexValidator(regex=r'\b\d{1,2}.\d{3}.\d{3}-[K|k|0-9]' )])
    Nombre = models.CharField(max_length=100, null=False, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    FechaIngreso = models.DateField(null=False)
    Correo = models.CharField(max_length=100, null=False, unique=True, validators=[EmailValidator])
    IdPerfil = models.ForeignKey(Perfil, on_delete=CASCADE, default=1)
    user = models.OneToOneField(User, unique=True, null=False, on_delete=CASCADE)
    IdSubGerencia = models.ForeignKey(SubGerencia, on_delete=CASCADE, default=1)
    Imagen = models.ImageField(default="foto_perfil.jpg", upload_to="usuarios", null=True, blank=True)

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
    NombreEvaluador = models.CharField(Empleado, max_length=100, null=True, blank=True)
    NombreCalibrador = models.CharField(Empleado, max_length=100, null=True, blank=True)
    IdEmpleado = models.ForeignKey(Empleado, on_delete=CASCADE)

    def __str__(self):
        return str(self.Rol)


class Evaluacion(models.Model):
    Estado = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    Fase = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    ComentarioCalibrador = models.CharField(max_length=80,  null=True, blank=True, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    FechaEvaluacion = models.DateTimeField(default=timezone.now)
    ComentarioEvaluador = models.CharField(max_length=100, null=True, blank=True,validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    Calificacion = models.IntegerField( null=True, blank=True, validators=[RegexValidator(regex=r'^[0-9]')])
    AutoEvaluacion = models.IntegerField( null=True, blank=True, validators=[RegexValidator(regex=r'^[0-9]')])
    IdEmpleado = models.ForeignKey(Empleado, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.Fase
class PlanAccion(models.Model):
    Accion = models.CharField(max_length=50, null=True, blank=True, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    Medicion = models.CharField(max_length=50, null=True, blank=True, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    IdEvaluacion = models.ForeignKey(Evaluacion, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.Accion
class DetalleEv(models.Model):
    FechaEvaluacion = models.DateTimeField(default=timezone.now)
    ComentarioEvaluador = models.CharField(max_length=100, null=True, blank=True,validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    Calificacion = models.IntegerField( null=True, blank=True, validators=[RegexValidator(regex=r'^[0-9]')])
    AutoEvaluacion = models.IntegerField( null=True, blank=True, validators=[RegexValidator(regex=r'^[0-9]')])
    IdEvaluacion = models.ForeignKey(Evaluacion, on_delete=CASCADE, default=1)
    IdPlanAccion = models.ForeignKey(PlanAccion, on_delete=CASCADE, default=1)

class Competencia(models.Model):
    NombreCompetencia = models.CharField(max_length=60, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    Definicion = models.CharField(max_length=1000, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    IdPerfil = models.ForeignKey(Perfil, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.NombreCompetencia

class AccionClave(models.Model):
    Descripcion = models.CharField(max_length=1000, validators=[RegexValidator(regex=r'^[a-zA-Z]' )])
    IdCompetencia = models.ForeignKey(Competencia, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.Descripcion

class EmpleadoEliminado(models.Model):
    Rut = models.CharField(max_length=12)
    Nombre = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    FechaEliminacion = models.DateField(auto_now=True)