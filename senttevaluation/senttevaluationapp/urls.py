from django.urls import path, include
from senttevaluationapp import views

urlpatterns = [
# ----------------------------------  Login ---------------------------------.
    path('', views.login, name="Login"),
# ----------------------------------  Administrador ---------------------------------------------.
    path('adminInicio', views.adminInicio, name="adminInicio"),
    path('adminAcciones', views.adminAcciones, name="adminAcciones"),
    path('adminCargos', views.adminCargos, name="adminCargos"),
    path('adminCompetencias', views.adminCompetencias, name="adminCompetencias"),
    path('adminGerencias', views.adminGerencias, name="adminGerencias"),
    path('adminSubgerencias', views.adminSubgerencias, name="adminSubgerencias"),
    path('adminUsuarios', views.adminUsuarios, name="adminUsuarios"),
    path('adminAyuda', views.adminAyuda, name="adminAyuda"),
    path('adminAccionesModificar/<int:accionclave_id>/', views.editarAcciones, name="adminAccionesModificar"),

# ----------------------------------  Evaluador ------------------------------------------------------.
    path('evaluadorInicio', views.evaluadorInicio, name="evaluadorInicio"),
    path('evaluadorEvaluacion', views.evaluadorEvaluacion, name="evaluadorEvaluacion"),
    path('evaluadorAutovaluacion', views.evaluadorAutovaluacion, name="evaluadorAutovaluacion"),
    path('evaluadorFormulario', views.evaluadorFormulario, name="evaluadorAutovaluacion"),
    path('evaluadorAyuda', views.evaluadorAyuda, name="evaluadorAyuda"),
# ----------------------------------  Colaborador ----------------------------------------------------.
    path('colaboradorInicio', views.colaboradorInicio, name="colaboradorInicio"),
    path('colaboradorAyuda', views.colaboradorAyuda, name="colaboradorAyuda"),
    path('colaboradorAutovaluacion', views.colaboradorAutovaluacion, name="colaboradorAutovaluacion"),
# ----------------------------------  Calibrador -----------------------------------------------------.
    path('calibradorInicio', views.calibradorInicio, name="calibradorInicio"),
    path('calibradorAyuda', views.calibradorAyuda, name="calibradorAyuda"),
    path('calibradorEvaluaciones', views.calibradorEvaluaciones, name="calibradorEvaluaciones"),
]