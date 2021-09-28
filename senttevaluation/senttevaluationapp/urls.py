from django.urls import path

from senttevaluationapp import views

urlpatterns = [
<<<<<<< HEAD
# ----------------------------------  Login ---------------------------------.
    path('', views.login, name="Login"),    
# ----------------------------------  Administrador ---------------------------------------------.
=======
    path('', views.login, name="Login"),
    path('evaluadorInicio', views.evaluadorInicio, name="evaluadorInicio"),
    path('evaluadorEvaluacion', views.evaluadorEvaluacion, name="evaluadorEvaluacion"),
    path('evaluadorAutovaluacion', views.evaluadorAutovaluacion, name="evaluadorAutovaluacion"),
    path('evaluadorFormulario', views.evaluadorFormulario, name="evaluadorFormulario"),
    path('evaluadorAyuda', views.evaluadorAyuda, name="evaluadorAyuda"),
>>>>>>> hans
    path('adminInicio', views.adminInicio, name="adminInicio"),
    path('adminAcciones', views.adminAcciones, name="adminAcciones"),
    path('adminCargos', views.adminCargos, name="adminCargos"),
    path('adminCompetencias', views.adminCompetencias, name="adminCompetencias"),
    path('adminGerencias', views.adminGerencias, name="adminGerencias"),
    path('adminSubgerencias', views.adminSubgerencias, name="adminSubgerencias"),
    path('adminUsuarios', views.adminUsuarios, name="adminUsuarios"),
    path('adminAyuda', views.adminAyuda, name="adminAyuda"),
# ----------------------------------  Evaluador ------------------------------------------------------.
    path('evaluadorInicio', views.evaluadorInicio, name="evaluadorInicio"),
    path('evaluadorEvaluacion', views.evaluadorEvaluacion, name="evaluadorEvaluacion"),
    path('evaluadorAutovaluacion', views.evaluadorAutovaluacion, name="evaluadorAutovaluacion"),
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