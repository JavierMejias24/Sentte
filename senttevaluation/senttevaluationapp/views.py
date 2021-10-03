from django.core.files.base import ContentFile
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import View
from .models import Cargo, AccionClave, Competencia, Gerencia, Empleado, SubGerencia, Perfil
from .forms import CompetenciaForm, EmpleadoForm, CargoForm, AccionesForm, GerenciaForm, SubgerenciaForm
# Create your views here.
# ----------------------------------  Login ---------------------------------.
def login(request):
    return render(request, "registration/login.html")

# ----------------------------------  Administrador ---------------------------------.

def adminInicio(request):
    return render(request, "admin/adminInicio.html")

# --1) Forma de llamar a todos los datos--.
def adminAcciones(request):
    accioneclaves = AccionClave.objects.all()
    contexto = {
        'accionclaves':accioneclaves,
        'form': AccionesForm()
    }
    if request.method == 'POST':
        formulario = AccionesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("adminAcciones")
        else:
            return render("admin/adminAcciones.html")
    return render(request, "admin/adminAcciones.html", contexto)

def editarAcciones(request, idAccionClave):
    acciones = AccionClave.objects.filter(id=idAccionClave).first()
    form = AccionesForm(instance=acciones)
    return render(request, "admin/adminAccionesModificar.html", {'form':form, 'acciones':acciones})

# --2) Forma de llamar a todos los datos--.
def adminCargos(request):
    cargos = Cargo.objects.all()
    contexto = {
        'cargos':cargos,
        'form': CargoForm()
    }
    if request.method == 'POST':
        formulario = CargoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            print("Agregado con exito")
            return HttpResponseRedirect("adminCargos")
        else:
            return render("admin/adminCargos.html")

    return render(request,"admin/adminCargos.html", contexto)


def adminCompetencias(request):
    competencias = Competencia.objects.all()
    contexto1 = {
        'competencias': competencias,
        'form': CompetenciaForm()
    }
    if request.method == 'POST':
        formulario = CompetenciaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("adminCompetencias")
        else:
            return render("admin/adminCompetencias.html")
    return render(request, "admin/adminCompetencias.html", contexto1)

def adminGerencias(request):
    gerencias = Gerencia.objects.all()
    contexto = {
        'gerencias': gerencias,
        'form': GerenciaForm()
    }
    if request.method == 'POST':
        formulario = GerenciaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("adminGerencias")
        else:
            return render("admin/adminGerencias.html")
    return render(request, "admin/adminGerencias.html", contexto)

def adminSubgerencias(request):
    subgerencias = SubGerencia.objects.all()
    contexto = {
        'subgerencias': subgerencias,
        'form': SubgerenciaForm()
    }
    if request.method == 'POST':
        formulario = SubgerenciaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("adminSubgerencias")
        else:
            return render("admin/adminSubgerencias.html")
    return render(request, "admin/adminSubgerencias.html", contexto)

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