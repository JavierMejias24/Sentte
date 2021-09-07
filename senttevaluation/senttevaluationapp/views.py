from django.shortcuts import render, HttpResponse

# Create your views here.
# ----------------------------------  Evaluador ---------------------------------.
def home(request):
    return render(request, "home.html")

def grupos(request):
    return render(request, "grupos.html")

def graficos(request):
    return render(request, "graficos.html")

def ayuda(request):
    return render(request, "ayuda.html")

def login(request):
    return render(request, "login.html")

# ----------------------------------  Administrador ---------------------------------.
def adminInicio(request):
    return render(request, "adminInicio.html")

def adminAcciones(request):
    return render(request, "adminAcciones.html")

def adminCargos(request):
    return render(request, "adminCargos.html")

def adminCompetencias(request):
    return render(request, "adminCompetencias.html")

def adminGerencias(request):
    return render(request, "adminGerencias.html")

def adminSubgerencias(request):
    return render(request, "adminSubgerencias.html")

def adminUsuarios(request):
    return render(request, "adminUsuarios.html")

def adminEvaluaciones(request):
    return render(request, "adminEvaluaciones.html")

def adminAyuda(request):
    return render(request, "adminAyuda.html")