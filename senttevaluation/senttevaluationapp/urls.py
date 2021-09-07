from django.urls import path

from senttevaluationapp import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('home', views.home, name="Home"),
    path('grupos', views.grupos, name="Grupos"),
    path('graficos', views.graficos, name="Graficos"),
    path('ayuda', views.ayuda, name="Ayuda"),
    path('adminInicio', views.adminInicio, name="adminInicio"),
    path('adminAcciones', views.adminAcciones, name="adminAcciones"),
    path('adminCargos', views.adminCargos, name="adminCargos"),
    path('adminCompetencias', views.adminCompetencias, name="adminCompetencias"),
    path('adminGerencias', views.adminGerencias, name="adminGerencias"),
    path('adminSubgerencias', views.adminSubgerencias, name="adminSubgerencias"),
    path('adminUsuarios', views.adminUsuarios, name="adminUsuarios"),
    path('adminEvaluaciones', views.adminEvaluaciones, name="adminEvaluaciones"),
    path('adminAyuda', views.adminAyuda, name="adminAyuda"),
]