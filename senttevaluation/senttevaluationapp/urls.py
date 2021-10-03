from django.urls import path, include
from senttevaluationapp import views

urlpatterns = [
# ----------------------------------  Login ---------------------------------.
    path('', views.login, name="Login"),
# ----------------------------------  Administrador ---------------------------------------------.
    path('adminInicio', views.adminInicio, name="adminInicio"),
    path('adminAcciones', views.adminAcciones, name="adminAcciones"),
    path('adminAccionesModificar/<id>/', views.editarAcciones, name="adminAccionesModificar"),
    path('adminAccionesEliminar/<id>/', views.eliminarAcciones, name="adminAccionesEliminar"),
    path('adminCargos', views.adminCargos, name="adminCargos"),
    path('adminCargosModificar/<id>/', views.editarCargos, name="adminCargosModificar"),
    path('adminCargosEliminar/<id>/', views.eliminarCargos, name="adminCargosEliminar"),
    path('adminCompetencias', views.adminCompetencias, name="adminCompetencias"),
    path('adminCompetenciasModificar/<id>/', views.editarCompetencias, name="adminCompetenciasModificar"),
    path('adminCompetenciasEliminar/<id>/', views.eliminarCompetencias, name="adminCompetenciasEliminar"),
    path('adminGerencias', views.adminGerencias, name="adminGerencias"),
    path('adminGerenciasModificar/<id>/', views.editarGerencias, name="adminGerenciasModificar"),
    path('adminGerenciasEliminar/<id>/', views.eliminarGerencias, name="adminGerenciasEliminar"),
    path('adminSubgerencias', views.adminSubgerencias, name="adminSubgerencias"),
    path('adminSubgerenciasModificar/<id>/', views.editarSubgerencia, name="adminSubgerenciasModificar"),
    path('adminSubgerenciasEliminar/<id>/', views.eliminarSubgerencia, name="adminSubgerenciasEliminar"),
    path('adminUsuarios', views.adminUsuarios, name="adminUsuarios"),
    path('adminUsuariosAgregar', views.agregarUsuario, name="adminUsuariosAgregar"),
    path('adminUsuariosModificar/<id>/', views.editarUsuario, name="adminUsuariosModificar"),
    path('adminUsuariosEliminar/<id>/', views.eliminarUsuario, name="adminUsuariosEliminar"),
    path('adminAyuda', views.adminAyuda, name="adminAyuda"),

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