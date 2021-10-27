from django.contrib import admin
from .models import *

# Register your models here.

# ----------------------------------  Area ---------------------------------.
admin.site.register(Area)
# ----------------------------------  Gerencia ---------------------------------.

admin.site.register(Gerencia)
# ----------------------------------  SubGerencia ---------------------------------.

admin.site.register(SubGerencia)
# ----------------------------------  Empleado ---------------------------------.

admin.site.register(Empleado)
# ----------------------------------  Perfil Rol ---------------------------------.

admin.site.register(PerfilRol)
# ----------------------------------  Cargo ---------------------------------.

admin.site.register(Cargo)
# ----------------------------------  Perfil ---------------------------------.

admin.site.register(Perfil)
# ----------------------------------  Evaluacion ---------------------------------.

admin.site.register(Evaluacion)
# ----------------------------------  Plan Accion ---------------------------------.

admin.site.register(PlanAccion)
# ----------------------------------  Detalle Evaluacion ---------------------------------.

admin.site.register(DetalleEv)
# ----------------------------------  Competencia ---------------------------------.

admin.site.register(Competencia)
# ----------------------------------  AccionClave ---------------------------------.

admin.site.register(AccionClave)