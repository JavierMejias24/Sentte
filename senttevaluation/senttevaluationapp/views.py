from django.shortcuts import render, HttpResponse

# Create your views here.
# ----------------------------------  Login ---------------------------------.
def login(request):
    return render(request, "login.html")

# ----------------------------------  Administrador ---------------------------------.
def adminInicio(request):
    return render(request, "admin/adminInicio.html")

def adminAcciones(request):
    return render(request, "admin/adminAcciones.html")

def adminCargos(request):
    return render(request, "admin/adminCargos.html")

def adminCompetencias(request):
    return render(request, "admin/adminCompetencias.html")

def adminGerencias(request):
    return render(request, "admin/adminGerencias.html")

def adminSubgerencias(request):
    return render(request, "admin/adminSubgerencias.html")

def adminUsuarios(request):
    return render(request, "admin/adminUsuarios.html")

def adminEvaluaciones(request):
    return render(request, "admin/adminEvaluaciones.html")

def adminAyuda(request):
    return render(request, "admin/adminAyuda.html")

# ----------------------------------  Evaluador ---------------------------------.
def evaluadorInicio(request):
    return render(request, "evaluador/evaluadorInicio.html")

def evaluadorEvaluacion(request):
    return render(request, "evaluador/evaluadorEvaluacion.html")

def evaluadorAutovaluacion(request):
    return render(request, "evaluador/evaluadorAutovaluacion.html")

def evaluadorAyuda(request):
    return render(request, "evaluador/evaluadorAyuda.html")

# ----------------------------------  Colaborador ---------------------------------.

def colaboradorInicio(request):
    return render(request, "colaborador/colaboradorInicio.html")

def colaboradorAyuda(request):
    return render(request, "colaborador/colaboradorAyuda.html")

def colaboradorAutovaluacion(request):
    return render(request, "colaborador/colaboradorAutovaluacion.html")

# ----------------------------------  Calibrador ---------------------------------.

def calibradorInicio(request):
    return render(request, "calibrador/calibradorInicio.html")
    
def calibradorAyuda(request):
    return render(request, "calibrador/calibradorAyuda.html")

def calibradorEvaluaciones(request):
    return render(request, "calibrador/calibradorEvaluaciones.html")