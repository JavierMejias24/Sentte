from django.contrib import admin
from .models import AREA, CARGOS, PERFIL_COMPETENCIAS, SUB_GERENCIA, GERENCIA, PERFIL, CUENTAS, EVALUACIONES, CUENTA_EVALUACION, COMPETENCIA_ASOCIADA, PLANES_DE_ACCION, ACCIONES_CLAVE

# Register your models here.

admin.site.register(AREA)
admin.site.register(CARGOS)
admin.site.register(PERFIL_COMPETENCIAS)
admin.site.register(SUB_GERENCIA)
admin.site.register(GERENCIA)
admin.site.register(PERFIL)
admin.site.register(CUENTAS)
admin.site.register(EVALUACIONES)
admin.site.register(CUENTA_EVALUACION)
admin.site.register(COMPETENCIA_ASOCIADA)
admin.site.register(PLANES_DE_ACCION)
admin.site.register(ACCIONES_CLAVE)