from django.db import models

# Create your models here.

class AREA(models.Model):
    NOMBRE = models.CharField(max_length=50)

    def __str__(self):
        return self.NOMBRE

class CARGOS(models.Model):
    NOMBRE = models.CharField(max_length=50)

    def __str__(self):
        return self.NOMBRE

class PERFIL_COMPETENCIAS(models.Model):
    NOMBRE = models.CharField(max_length=50)

    def __str__(self):
        return self.NOMBRE

class SUB_GERENCIA(models.Model):
    NOMBRE = models.CharField(max_length=50)

    def __str__(self):
        return self.NOMBRE

class GERENCIA(models.Model):
    NOMBRE = models.CharField(max_length=50)

    def __str__(self):
        return self.NOMBRE

class PERFIL(models.Model):
    NOMBRE = models.CharField(max_length=50)
    CORREO = models.CharField(max_length=50)
    FECHA_INGRESO = models.DateField()
    FECHA_ANTIGUEDAD = models.CharField(max_length=50)
    ID_SUB_GERENCIA = models.ForeignKey(SUB_GERENCIA, on_delete=models.PROTECT)
    ID_GERENCIA = models.ForeignKey(GERENCIA, on_delete=models.PROTECT)
    ID_AREA = models.ForeignKey(AREA, on_delete=models.PROTECT)
    ID_PERFIL_COMPETENCIAS = models.ForeignKey(PERFIL_COMPETENCIAS, on_delete=models.PROTECT)
    ID_CARGO = models.ForeignKey(CARGOS, on_delete=models.PROTECT)

    def __str__(self):
        return self.NOMBRE

class CUENTAS(models.Model):
    RUT = models.CharField(max_length=13)
    CONTRASEÑA = models.CharField(max_length=80)
    ID_PERFILES = models.ForeignKey(PERFIL, on_delete=models.PROTECT)

class EVALUACIONES(models.Model):
    ESTADO = models.CharField(max_length=1)
    COMPETENCIAS = models.CharField(max_length=40)
    CALIFICACION = models.IntegerField()
    COMENTARIOS = models.CharField(max_length=100)
    TIPO_COMPETENCIA = models.CharField(max_length=30)
    ACCION = models.CharField(max_length=30)
    MEDICION = models.CharField(max_length=30)

class CUENTA_EVALUACION(models.Model):
    ROL = models.CharField(max_length=30)
    ID_CUENTA = models.ForeignKey(CUENTAS, on_delete=models.PROTECT)
    ID_EVALUACIONES = models.ForeignKey(EVALUACIONES, on_delete=models.PROTECT)

class COMPETENCIA_ASOCIADA(models.Model):
    NOMBRE = models.CharField(max_length=50)
    DEFINICION = models.CharField(max_length=100)
    ID_EVALUACIONES = models.ForeignKey(EVALUACIONES, on_delete=models.PROTECT)

    def __str__(self):
        return self.NOMBRE
    
class PLANES_DE_ACCION(models.Model):
    ACCION = models.CharField(max_length=200)
    MEDICION = models.CharField(max_length=200)
    ID_EVALUACIONES = models.ForeignKey(EVALUACIONES, on_delete=models.PROTECT)
    ID_COMPETENCIA_ASOCIADA = models.ForeignKey(COMPETENCIA_ASOCIADA, on_delete=models.PROTECT)

class ACCIONES_CLAVE(models.Model):
    DESCRIPCIÓN = models.CharField(max_length=100)
    PUNTUACIÓN = models.IntegerField()
    ID_COMPETENCIA_ASOCIADA = models.ForeignKey(COMPETENCIA_ASOCIADA, on_delete=models.PROTECT)