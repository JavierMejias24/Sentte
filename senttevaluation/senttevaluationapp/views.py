from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import Cargo, AccionClave, Competencia, Gerencia, Empleado, SubGerencia
from .forms import EmpleadoForm
# Create your views here.
# ----------------------------------  Login ---------------------------------.
def login(request):
    return render(request, "registration/login.html")

# ----------------------------------  Administrador ---------------------------------.

def adminInicio(request):
    return render(request, "admin/adminInicio.html")

# --1) Forma de llamar a todos los datos--.
def adminAcciones(request):
    accionclaves = AccionClave.objects.all()
    return render(request, "admin/adminAcciones.html", {'accionclaves':accionclaves})

# --2) Forma de llamar a todos los datos--.
def adminCargos(request):
    cargos = Cargo.objects.all()
    contexto = {
        'cargos':cargos
    }
    return render(request, "admin/adminCargos.html",contexto)

def adminCompetencias(request):
    competencias = Competencia.objects.all()
    return render(request, "admin/adminCompetencias.html", {'competencias':competencias})

def adminGerencias(request):
    gerencias = Gerencia.objects.all()
    return render(request, "admin/adminGerencias.html", {'gerencias':gerencias})

def adminSubgerencias(request):
    subgerencias = SubGerencia.objects.all()
    return render(request, "admin/adminSubgerencias.html", {'subgerencias':subgerencias})

def adminUsuarios(request):
    empleados = Empleado.objects.all()
    return render(request, "admin/adminUsuarios.html", {'empleados':empleados})

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

def evaluadorFormulario(request):
    return render(request, "evaluador/evaluadorFormulario.html")

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