from django.contrib import admin
from .models import Area, Gerencia, SubGerencia, Empleado, PerfilRol, Cargo, Perfil, Evaluacion, PlanAccion, DetalleEv, AccionClave, Competencia, AccionClave

# Register your models here.


# ----------------------------------  Area ---------------------------------.
admin.site.register(Area)
# ----------------------------------  Gerencia ---------------------------------.
class GerenciaAdmin(admin.ModelAdmin):
    list_display = ['NombreGerencia', 'IdArea']
    list_editable = ['IdArea']

admin.site.register(Gerencia, GerenciaAdmin)
# ----------------------------------  SubGerencia ---------------------------------.
class SubGerenciaAdmin(admin.ModelAdmin):
    list_display = ['NombreSubgerencia', 'IdGerencia']
    list_editable = ['IdGerencia']

admin.site.register(SubGerencia, SubGerenciaAdmin)
# ----------------------------------  Empleado ---------------------------------.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['Rut', 'Nombre', 'Contraseña', 'Correo', 'IdSubGerencia', 'IdRol']
    list_editable = ['Nombre', 'Contraseña', 'Correo', 'IdSubGerencia', 'IdRol']

admin.site.register(Empleado, EmpleadoAdmin)
# ----------------------------------  Perfil Rol ---------------------------------.
class PerfilRolAdmin(admin.ModelAdmin):
    list_display = ['Rol', 'RelacionEvaluado', 'NombreEvaluador', 'NombreCalibrador']
    list_editable = ['RelacionEvaluado', 'NombreEvaluador', 'NombreCalibrador']

admin.site.register(PerfilRol, PerfilRolAdmin)
# ----------------------------------  Cargo ---------------------------------.
class PerfilRolAdmin(admin.ModelAdmin):
    list_display = ['Rol', 'RelacionEvaluado', 'NombreEvaluador', 'NombreCalibrador']
    list_editable = ['RelacionEvaluado', 'NombreEvaluador', 'NombreCalibrador']

admin.site.register(Cargo)
# ----------------------------------  Perfil ---------------------------------.
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['NombrePerfil', 'IdCargo']
    list_editable = ['IdCargo']

admin.site.register(Perfil, PerfilAdmin)
# ----------------------------------  Evaluacion ---------------------------------.
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ['Estado', 'Fase', 'ComentarioCalibrador', 'IdPerfil', 'IdEmpleado']
    list_editable = ['Fase', 'IdPerfil', 'IdEmpleado']

admin.site.register(Evaluacion, EvaluacionAdmin)
# ----------------------------------  Plan Accion ---------------------------------.
class PlanAccionAdmin(admin.ModelAdmin):
    list_display = ['Accion', 'Medicion']

admin.site.register(PlanAccion, PlanAccionAdmin)
# ----------------------------------  Detalle Evaluacion ---------------------------------.
class DetalleEvAdmin(admin.ModelAdmin):
    list_display = ['FechaEvaluacion', 'ComentarioEvaluador', 'Calificacion', 'AutoEvaluacion' ,'IdEvaluacion', 'IdPlanAccion']
    list_editable = ['IdEvaluacion', 'IdPlanAccion']

admin.site.register(DetalleEv, DetalleEvAdmin)
# ----------------------------------  Competencia ---------------------------------.
class CompetenciasAdmin(admin.ModelAdmin):
    list_display = ['NombreCompetencia', 'Definicion', 'IdPerfil']
    list_editable = ['Definicion', 'IdPerfil']

admin.site.register(Competencia, CompetenciasAdmin)
# ----------------------------------  AccionClave ---------------------------------.
class AccionClaveAdmin(admin.ModelAdmin):
    list_display = ['Descripcion', 'IdCompetencia']
    list_editable = ['IdCompetencia']

admin.site.register(AccionClave)