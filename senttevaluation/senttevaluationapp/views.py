from django.core.files.base import ContentFile
from django.db.models.query import InstanceCheckMeta
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
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

# -- ------------Acciones Claves----------------.
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

def editarAcciones(request, id):
    acciones = get_object_or_404(AccionClave, id=id)
    data = {
        'form':  AccionesForm(instance=acciones)
    }
    if request.method == 'POST':
        formulario = AccionesForm(data=request.POST, instance=acciones)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="adminAcciones")
        else:
            data["form"] = formulario
    return render(request, "admin/adminAccionesModificar.html", data)

def eliminarAcciones(request, id):
    acciones = get_object_or_404(AccionClave, id=id)
    acciones.delete()
    return redirect(to='adminAcciones')
# -----------------------------------------------------------------------------------------------.

# -- ------------ Cargos ----------------.
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

def editarCargos(request, id):
    cargos = get_object_or_404(Cargo, id=id)
    data = {
        'form':  CargoForm(instance=cargos)
    }
    if request.method == 'POST':
        formulario = CargoForm(data=request.POST, instance=cargos)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="adminCargos")
        else:
            data["form"] = formulario
    return render(request, "admin/adminCargosModificar.html", data)

def eliminarCargos(request, id):
    cargos = get_object_or_404(Cargo, id=id)
    cargos.delete()
    return redirect(to="adminCargos")

# -----------------------------------------------------------------------------------------------.

# -- ------------ Competencias ----------------.
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

def editarCompetencias(request, id):
    competencias = get_object_or_404(Competencia, id=id)
    data = {
        'form':  CompetenciaForm(instance=competencias)
    }
    if request.method == 'POST':
        formulario = CompetenciaForm(data=request.POST, instance=competencias)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="adminCompetencias")
        else:
            data["form"] = formulario
    return render(request, "admin/adminCompetenciasModificar.html", data)

def eliminarCompetencias(request, id):
    competencias = get_object_or_404(Competencia, id=id)
    competencias.delete()
    return redirect(to="adminCompetencias")

# -----------------------------------------------------------------------------------------------.

# -- ------------ Gerencias ----------------.
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

def editarGerencias(request, id):
    gerencias = get_object_or_404(Gerencia, id=id)
    data = {
        'form':  GerenciaForm(instance=gerencias)
    }
    if request.method == 'POST':
        formulario = GerenciaForm(data=request.POST, instance=gerencias)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="adminGerencias")
        else:
            data["form"] = formulario
    return render(request, "admin/adminGerenciasModificar.html", data)

def eliminarGerencias(request, id):
    gerencias = get_object_or_404(Gerencia, id=id)
    gerencias.delete()
    return redirect(to="adminGerencias")
# -----------------------------------------------------------------------------------------------.

# -- ------------ Sub-gerencias ----------------.
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

def editarSubgerencia(request, id):
    subgerencias = get_object_or_404(SubGerencia, id=id)
    data = {
        'form':  SubgerenciaForm(instance=subgerencias)
    }
    if request.method == 'POST':
        formulario = SubgerenciaForm(data=request.POST, instance=subgerencias)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="adminSubgerencias")
        else:
            data["form"] = formulario
    return render(request, "admin/adminSubgerenciasModificar.html", data)

def eliminarSubgerencia(request, id):
    subgerencias = get_object_or_404(SubGerencia, id=id)
    subgerencias.delete()
    return redirect(to="adminSubgerencias")
# -----------------------------------------------------------------------------------------------.

# -- ------------ Empleado ----------------.
def adminUsuarios(request):
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("adminUsuarios")
        
    return render(request, "admin/adminUsuarios.html", {'empleados':empleados})

def agregarUsuario(request):
    data = {
        'form': EmpleadoForm()
    }
    return render(request, 'admin/adminUsuarioAgregar.html')

def editarUsuario(request, id):
    empleados = get_object_or_404(Empleado, id=id)
    data = {
        'form':  EmpleadoForm(instance=empleados)
    }
    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleados)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="adminUsuarios")
        else:
            data["form"] = formulario
    return render(request, "admin/adminUsuariosModificar.html", data)

def eliminarUsuario(request, id):
    empleados = get_object_or_404(Empleado, id=id)
    empleados.delete()
    return redirect(to="adminUsuarios")

# -----------------------------------------------------------------------------------------------.

def adminAyuda(request):
    return render(request, "admin/adminAyuda.html")

# -----------------------------------------------------------------------------------------------.

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