from django.contrib import admin
from .models import Area, Gerencia, SubGerencia, Empleado, PerfilRol, Cargo, Perfil, Evaluacion, PlanAccion, DetalleEv, AccionClave, Competencia, AccionClave

# Register your models here.

admin.site.register(Area)
admin.site.register(Gerencia)
admin.site.register(SubGerencia)
admin.site.register(Empleado)
admin.site.register(PerfilRol)
admin.site.register(Cargo)
admin.site.register(Perfil)
admin.site.register(Evaluacion)
admin.site.register(PlanAccion)
admin.site.register(DetalleEv)
admin.site.register(Competencia)
admin.site.register(AccionClave)