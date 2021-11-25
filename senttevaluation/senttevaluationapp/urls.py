from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from senttevaluationapp import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
# ----------------------------------  Login ---------------------------------.
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
# ----------------------------------  Administrador ---------------------------------------------.
    path('home', views.admin_inicio, name="home"),
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
    path('adminArea', views.admin_areas, name="adminArea"),
    path('adminAgregarArea', views.agregar_areas, name="adminAgregarArea"),
    path('adminAreaModificar/<id>/', views.editar_area, name="adminAreaModificar"),
    path('adminAreaEliminar/<id>/', views.eliminar_area, name="adminAreaEliminar"),
    path('adminIndicadores', views.admin_indicadores, name="adminIndicadores"),
    path('adminAyuda', views.admin_ayuda, name="adminAyuda"),
# ----------------------------------  Evaluador ------------------------------------------------------.
    path('evaluadorInicio', views.evaluador_inicio, name="evaluadorInicio"),
    path('evaluadorEvaluacion', views.evaluador_evaluacion, name="evaluadorEvaluacion"),
    path('evaluadorAutovaluacion/<id>', views.evaluador_autovaluacion, name="evaluadorAutovaluacion"),
    path('evaluadorAutovaluacion2/<id>', views.evaluador_autovaluacion2, name="evaluadorAutovaluacion2"),
    path('evaluadorFormulario/<id>', views.evaluador_formulario, name="evaluadorFormulario"),
    path('evaluadorFormulario2/<id>', views.evaluador_formulario2, name="evaluadorFormulario2"),
    path('evaluadorFormulario3/<id>', views.evaluador_formulario3, name="evaluadorFormulario3"),
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)