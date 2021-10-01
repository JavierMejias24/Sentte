from django.db import models
from django.db.models.deletion import PROTECT
from django.core.exceptions import ValidationError

# Create your models here.

class AREA(models.Model):
    NombreArea = models.CharField(max_length=50)

    def __str__(self):
        return self.NombreArea

class GERENCIA(models.Model):
    NombreGerencia = models.CharField(max_length=50)
    IdArea = models.ForeignKey(AREA, on_delete=models.PROTECT)

    def __str__(self):
        return self.NombreGerencia

class SUBGERENCIA(models.Model):
    NombreSubgerencia = models.CharField(max_length=50)
    IdGerencia = models.ForeignKey(GERENCIA, on_delete=models.PROTECT)

    def __str__(self):
        return self.NombreSubgerencia

class EVALUADOR(models.Model):
    NombreEvaluador = models.CharField(max_length=60)
    IdSubGerencia = models.ForeignKey(SUBGERENCIA, on_delete=PROTECT)

    def __str__(self):
        return self.NombreEvaluador

class CALIBRADOR(models.Model):
    NombreCalibrador = models.CharField(max_length=60)

    def __str__(self):
        return self.NombreCalibrador

class PLANACCION(models.Model):
    Accion = models.CharField(max_length=200)
    Medicion = models.CharField(max_length=200)

class CARGO(models.Model):
    NombreCargo = models.CharField(max_length=50)

    def __str__(self):
        return self.NombreCargo

class PERFIL(models.Model):
    NombrePerfil = models.CharField(max_length=50)

    def __str__(self):
        return self.NombrePerfil

class PERFILCARGO(models.Model):
    IdCargo = models.ForeignKey(CARGO, on_delete=PROTECT)
    IdPerfil = models.ForeignKey(PERFIL, on_delete=PROTECT)

class EMPLEADO(models.Model):
    Rut = models.CharField(max_length=12, unique=True)
    Nombre = models.CharField(max_length=60)
    Usuario = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)
    Rol = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Nombre

class EVALUADO(models.Model):
    FechaIngreso = models.DateField()
    IdEmpleado = models.ForeignKey(EMPLEADO, on_delete=PROTECT)
    IdSubGerencia = models.ForeignKey(SUBGERENCIA, on_delete=PROTECT)

class EVALUACION(models.Model):
    Estado = models.CharField(max_length=50)
    Fase = models.CharField(max_length=50)
    IdPerfil = models.ForeignKey(PERFIL, on_delete=PROTECT)
    IdEvaluado = models.ForeignKey(EVALUADO, on_delete=PROTECT)

class ENCARGADO(models.Model):
    IdEvaluador = models.ForeignKey(EVALUADOR, on_delete=PROTECT)
    IdEvaluacion = models.ForeignKey(EVALUACION, on_delete=PROTECT)
    IdCalibrador = models.ForeignKey(CALIBRADOR, on_delete=PROTECT)
    Fecha = models.DateField()
    RelacionEvaluado = models.CharField(max_length=50)
    Comentario = models.CharField(max_length=200)

class ACCIONCLAVE(models.Model):
    Descripcion = models.CharField(max_length=1000)

class COMPETENCIA(models.Model):
    NombreCompetencia = models.CharField(max_length=50)
    Definicion = models.CharField(max_length=1000)

class COMPACC(models.Model):
    IdCompetencia = models.ForeignKey(COMPETENCIA, on_delete=PROTECT)
    IdAccionClave = models.ForeignKey(ACCIONCLAVE, on_delete=PROTECT)

class PERFCOMP(models.Model):
    IdPerfil = models.ForeignKey(PERFIL, on_delete=PROTECT)
    IdCompetencia = models.ForeignKey(COMPETENCIA, on_delete=PROTECT)

class DETALLEEV(models.Model):
    FechaEvaluacion = models.DateField()
    ComentarioEvaluador = models.CharField(max_length=100)
    Calificacion = models.IntegerField()
    AutoEvaluacion = models.IntegerField()
    IdEvaluacion = models.ForeignKey(EVALUACION, on_delete=PROTECT)
    IdPlanaccion = models.ForeignKey(PLANACCION, on_delete=PROTECT)