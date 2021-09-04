from django.urls import path

from senttevaluationapp import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('home', views.home, name="Home"),
    path('grupos', views.grupos, name="Grupos"),
    path('graficos', views.graficos, name="Graficos"),
    path('ayuda', views.ayuda, name="Ayuda"),
    path('index', views.index, name="Index"),
]