from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.

class Area(models.Model):
    NombreArea = models.CharField(max_length=50)

    def __str__(self):
        return self.NombreArea

class Gerencia(models.Model):
    NombreGerencia = models.CharField(max_length=50)
    IdArea = models.ForeignKey(Area, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.NombreGerencia

class SubGerencia(models.Model):
    NombreSubgerencia = models.CharField(max_length=50)
    IdGerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.NombreSubgerencia
    
class PerfilRol(models.Model):
    Roles = [
        (1, "Evaluador"),
        (2, "Evaluado"),
        (3, "Calibrador"),
    ]
    Rol = models.IntegerField(choices=Roles, default=1)
    RelacionEvaluado = models.CharField(max_length=50)
    NombreEvaluador = models.CharField(max_length=50, blank=True, default='')
    NombreCalibrador = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.get_Rol_display()

class Empleado(models.Model):
    Rut = models.CharField(max_length=12, unique=True)
    Nombre = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50, unique=True)
    IdSubGerencia = models.ForeignKey(SubGerencia, on_delete=CASCADE, default=1)
    IdRol = models.ForeignKey(PerfilRol, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.Nombre 

class Cargo(models.Model):
    NombreCargo = models.CharField(max_length=50)

    def __str__(self):
        return self.NombreCargo

class Perfil(models.Model):
    NombrePerfil = models.CharField(max_length=50)
    IdCargo = models.ForeignKey(Cargo, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.NombrePerfil

class Evaluacion(models.Model):
    Estado = models.CharField(max_length=50)
    Fase = models.CharField(max_length=50)
    ComentarioCalibrador = models.CharField(max_length=50)
    IdPerfil = models.ForeignKey(Perfil, on_delete=CASCADE, default=1)
    IdEmpleado = models.ForeignKey(Empleado, on_delete=CASCADE, default=1)

class PlanAccion(models.Model):
    Accion = models.CharField(max_length=50)
    Medicion = models.CharField(max_length=50)

class DetalleEv(models.Model):
    FechaEvaluacion = models.DateField()
    ComentarioEvaluador = models.CharField(max_length=100)
    Calificacion = models.IntegerField()
    AutoEvaluacion = models.IntegerField()
    IdEvaluacion = models.ForeignKey(Evaluacion, on_delete=CASCADE, default=1)
    IdPlanAccion = models.ForeignKey(PlanAccion, on_delete=CASCADE, default=1)

class Competencia(models.Model):
    NombreCompetencia = models.CharField(max_length=50)
    Definicion = models.CharField(max_length=1000)
    IdPerfil = models.ForeignKey(Perfil, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.NombreCompetencia

class AccionClave(models.Model):
    Descripcion = models.CharField(max_length=1000)
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