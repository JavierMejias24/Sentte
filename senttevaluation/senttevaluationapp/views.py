from django.shortcuts import render, HttpResponse

# Create your views here.
# ----------------------------------  Evaluador ---------------------------------.
def evaluadorInicio(request):
    return render(request, "evaluadorInicio.html")

def evaluadorEvaluacion(request):
    return render(request, "evaluadorEvaluacion.html")

def evaluadorAutovaluacion(request):
    return render(request, "evaluadorAutovaluacion.html")

def evaluadorAyuda(request):
    return render(request, "evaluadorAyuda.html")

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

# ----------------------------------  Colaborador ---------------------------------.

def colaboradorInicio(request):
    return render(request, "colaboradorInicio.html")

def colaboradorAyuda(request):
    return render(request, "colaboradorAyuda.html")

def colaboradorAutovaluacion(request):
    return render(request, "colaboradorAutovaluacion.html")

# ----------------------------------  Colaborador ---------------------------------.

def calibradorInicio(request):
    return render(request, "calibradorInicio.html")
    
def calibradorAyuda(request):
    return render(request, "calibradorAyuda.html")

def calibradorEvaluaciones(request):
    return render(request, "calibradorEvaluaciones.html")