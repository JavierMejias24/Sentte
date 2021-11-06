from django.urls import path
from senttevaluationapp import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
# ----------------------------------  Login ---------------------------------.
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
# ----------------------------------  Administrador ---------------------------------------------.
    path('adminInicio', views.admin_inicio, name="adminInicio"),
    path('adminAcciones', views.admin_acciones, name="adminAcciones"),
    path('adminAgregarAcciones', views.agregar_acciones, name="adminAgregarAcciones"),
    path('adminAccionesModificar/<id>/', views.editar_acciones, name="adminAccionesModificar"),
    path('adminAccionesEliminar/<id>/', views.eliminar_acciones, name="adminAccionesEliminar"),
    path('adminCargos', views.admin_cargos, name="adminCargos"),
    path('adminAgregarCargos', views.agregar_cargos, name="adminAgregarCargos"),
    path('adminCargosModificar/<id>/', views.editar_cargos, name="adminCargosModificar"),
    path('adminCargosEliminar/<id>/', views.eliminar_cargos, name="adminCargosEliminar"),
    path('adminCompetencias', views.admin_competencias, name="adminCompetencias"),
    path('adminAgregarCompetencias', views.agregar_competencias, name="adminAgregarCompetencias"),
    path('adminCompetenciasModificar/<id>/', views.editar_competencias, name="adminCompetenciasModificar"),
    path('adminCompetenciasEliminar/<id>/', views.eliminar_competencias, name="adminCompetenciasEliminar"),
    path('adminGerencias', views.admin_gerencias, name="adminGerencias"),
    path('adminAgregarGerencias', views.agregar_gerencias, name="adminAgregarGerencias"),
    path('adminGerenciasModificar/<id>/', views.editar_gerencias, name="adminGerenciasModificar"),
    path('adminGerenciasEliminar/<id>/', views.eliminar_gerencias, name="adminGerenciasEliminar"),
    path('adminSubgerencias', views.admin_subgerencias, name="adminSubgerencias"),
    path('adminAgregarSubgerencias', views.agregar_subgerencias, name="adminAgregarSubgerencias"),
    path('adminSubgerenciasModificar/<id>/', views.editar_subgerencia, name="adminSubgerenciasModificar"),
    path('adminSubgerenciasEliminar/<id>/', views.eliminar_subgerencia, name="adminSubgerenciasEliminar"),
    path('adminUsuarios', views.admin_usuarios, name="adminUsuarios"),
    path('adminAgregarUsuarios', views.agregar_usuario, name="adminAgregarUsuarios"),
    path('adminUsuariosModificar/<id>/', views.editar_usuario, name="adminUsuariosModificar"),
    path('adminUsuariosEliminar/<id>/', views.eliminar_usuario, name="adminUsuariosEliminar"),
    path('adminPerfil', views.admin_perfil, name="adminPerfil"),
    path('adminAgregarPerfil', views.agregar_perfil, name="adminAgregarPerfil"),
    path('adminModificarPerfil/<id>/', views.editar_perfil, name="adminModificarPerfil"),
    path('adminEliminarPerfil/<id>/', views.eliminar_perfil, name="adminEliminarPerfil"),
    path('adminAyuda', views.admin_ayuda, name="adminAyuda"),
# ----------------------------------  Evaluador ------------------------------------------------------.
    path('evaluadorInicio', views.evaluador_inicio, name="evaluadorInicio"),
    path('evaluadorEvaluacion', views.evaluador_evaluacion, name="evaluadorEvaluacion"),
    path('evaluadorAutovaluacion', views.evaluador_autovaluacion, name="evaluadorAutovaluacion"),
    path('evaluadorAgregarPlanAccion', views.guardar_planaccion, name="evaluadorAgregarPlanAccion"),
    path('evaluadorFormulario/<id>', views.evaluador_formulario, name="evaluadorFormulario"),
    path('evaluadorAyuda', views.evaluador_ayuda, name="evaluadorAyuda"),
# ----------------------------------  Colaborador ----------------------------------------------------.
    path('colaboradorInicio', views.colaborador_inicio, name="colaboradorInicio"),
    path('colaboradorAyuda', views.colaborador_ayuda, name="colaboradorAyuda"),
    path('colaboradorAutovaluacion', views.colaborador_autovaluacion, name="colaboradorAutovaluacion"),
# ----------------------------------  Calibrador -----------------------------------------------------.
    path('calibradorInicio', views.calibrador_inicio, name="calibradorInicio"),
    path('calibradorAyuda', views.calibrador_ayuda, name="calibradorAyuda"),
    path('calibradorEvaluaciones', views.calibrador_evaluaciones, name="calibradorEvaluaciones"),
]