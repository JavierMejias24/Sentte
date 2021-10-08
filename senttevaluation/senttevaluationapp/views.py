from django.core.files.base import ContentFile
from django.db.models.query import InstanceCheckMeta
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views.generic import View
from .models import Cargo, AccionClave, Competencia, DetalleEv, Gerencia, Empleado, PerfilRol, SubGerencia, Perfil
from .forms import CompetenciaForm, EmpleadoForm, CargoForm, AccionesForm, EvaluacionForm, GerenciaForm, PerfilRolForm, SubgerenciaForm, LoginForm

# Create your views here.
# ----------------------------------  Login ---------------------------------.
def login(request):
    empleados = Empleado.objects.all() 
    contexto = {
        'empleados':empleados,
        'form': LoginForm()
    }
    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        if formulario.is_valid():
            return render(request, "admin/adminInicio.html")
        else:
            return HttpResponseRedirect("login.html")
    return render(request, "login.html", contexto)

# ----------------------------------  Administrador ---------------------------------.

def admin_inicio(request):
    return render(request, "admin/adminInicio.html")

# -- ------------Acciones Claves----------------.
def admin_acciones(request):
    accioneclaves = AccionClave.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(accioneclaves, 8)
        accioneclaves = paginator.page(page)
    except:
        raise Http404

    contexto = {
        'entity':accioneclaves,
        'form': AccionesForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        formulario = AccionesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="adminAcciones")
        else:
            return HttpResponseRedirect("adminAcciones")
    return render(request, "admin/adminAcciones.html", contexto)

def editar_acciones(request, id):
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

def eliminar_acciones(request, id):
    acciones = get_object_or_404(AccionClave, id=id)
    acciones.delete()
    return redirect(to='adminAcciones')
# -----------------------------------------------------------------------------------------------.

# -- ------------ Cargos ----------------.
def admin_cargos(request):
    cargos = Cargo.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(cargos, 8)
        cargos = paginator.page(page)
    except:
        raise Http404

    contexto = {
        'entity':cargos,
        'form': CargoForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        formulario = CargoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            print("Agregado con exito")
            return HttpResponseRedirect("adminCargos")
        else:
            return HttpResponseRedirect("adminCargos")
    return render(request,"admin/adminCargos.html", contexto)

def editar_cargos(request, id):
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

def eliminar_cargos(request, id):
    cargos = get_object_or_404(Cargo, id=id)
    cargos.delete()
    return redirect(to="adminCargos")

# -----------------------------------------------------------------------------------------------.

# -- ------------ Competencias ----------------.
def admin_competencias(request):
    competencias = Competencia.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(competencias, 8)
        competencias = paginator.page(page)
    except:
        raise Http404

    contexto = {
        'entity': competencias,
        'form': CompetenciaForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        formulario = CompetenciaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("adminCompetencias")
        else:
            return HttpResponseRedirect("adminCompetencias")
    return render(request, "admin/adminCompetencias.html", contexto)

def editar_competencias(request, id):
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

def eliminar_competencias(request, id):
    competencias = get_object_or_404(Competencia, id=id)
    competencias.delete()
    return redirect(to="adminCompetencias")

# -----------------------------------------------------------------------------------------------.

# -- ------------ Gerencias ----------------.
def admin_gerencias(request):
    gerencias = Gerencia.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(gerencias, 8)
        gerencias = paginator.page(page)
    except:
        raise Http404

    contexto = {
        'entity': gerencias,
        'form': GerenciaForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        formulario = GerenciaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("adminGerencias")
        else:
            return HttpResponseRedirect("adminGerencias")
    return render(request, "admin/adminGerencias.html", contexto)

def editar_gerencias(request, id):
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

def eliminar_gerencias(request, id):
    gerencias = get_object_or_404(Gerencia, id=id)
    gerencias.delete()
    return redirect(to="adminGerencias")
# -----------------------------------------------------------------------------------------------.

# -- ------------ Sub-gerencias ----------------.
def admin_subgerencias(request):
    subgerencias = SubGerencia.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(subgerencias, 8)
        subgerencias = paginator.page(page)
    except:
        raise Http404

    contexto = {
        'entity': subgerencias,
        'form': SubgerenciaForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        formulario = SubgerenciaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("adminSubgerencias")
        else:
            return HttpResponseRedirect("adminSubgerencias")
    return render(request, "admin/adminSubgerencias.html", contexto)

def editar_subgerencia(request, id):
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

def eliminar_subgerencia(request, id):
    subgerencias = get_object_or_404(SubGerencia, id=id)
    subgerencias.delete()
    return redirect(to="adminSubgerencias")
# -----------------------------------------------------------------------------------------------.

# -- ------------ Empleado ----------------.
def admin_usuarios(request):
    empleados = Empleado.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(empleados, 8)
        empleados = paginator.page(page)
    except:
        raise Http404

    contexto = {
        'entity': empleados,
        'form': EmpleadoForm(), 
        'form1': PerfilRolForm(),
        'paginator': paginator
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST)
        formulario1 = PerfilRolForm(data=request.POST)
        if formulario.is_valid():
            if formulario1.is_valid():
                formulario.save()
                formulario1.save()
                return HttpResponseRedirect("adminUsuarios")
            else:
              return HttpResponseRedirect("adminUsuarios")  
        else:
            return HttpResponseRedirect("adminUsuarios")
    return render(request, "admin/adminUsuarios.html",contexto)

def editar_usuario(request, id):
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

def eliminar_usuario(request, id):
    empleados = get_object_or_404(Empleado, id=id)
    empleados.delete()
    return redirect(to="adminUsuarios")

# -----------------------------------------------------------------------------------------------.

def admin_ayuda(request):
    return render(request, "admin/adminAyuda.html")

# -----------------------------------------------------------------------------------------------.

# ----------------------------------  Evaluador ---------------------------------.
def evaluador_inicio(request):
    return render(request, "evaluador/evaluadorInicio.html")

def evaluador_evaluacion(request):
    empleados = Empleado.objects.all()
    return render(request, "evaluador/evaluadorEvaluacion.html", {'empleados':empleados})

def evaluador_autovaluacion(request):
    return render(request, "evaluador/evaluadorAutovaluacion.html")

def evaluador_ayuda(request):
    return render(request, "evaluador/evaluadorAyuda.html")

def evaluador_formulario(request):
    competencias = Competencia.objects.all()
    accionclaves = AccionClave.objects.all()
    contexto = {
        'competencias':competencias,
        'accionclaves':accionclaves,
    }
    return render(request, "evaluador/evaluadorFormulario.html", contexto)

# ----------------------------------  Colaborador ---------------------------------.

def colaborador_inicio(request):
    return render(request, "colaborador/colaboradorInicio.html")

def colaborador_ayuda(request):
    return render(request, "colaborador/colaboradorAyuda.html")

def colaborador_autovaluacion(request):
    return render(request, "colaborador/colaboradorAutovaluacion.html")

# ----------------------------------  Calibrador ---------------------------------.

def calibrador_inicio(request):
    return render(request, "calibrador/calibradorInicio.html")
    
def calibrador_ayuda(request):
    return render(request, "calibrador/calibradorAyuda.html")

def calibrador_evaluaciones(request):
    return render(request, "calibrador/calibradorEvaluaciones.html")