from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.db.models.query import InstanceCheckMeta
from django.db.models.query_utils import Q
from django.http.request import HttpRequest
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views.generic import View
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
# ----------------------------------  Login ---------------------------------.
def login(request):

    usuario = request.POST.get('name')
    contraseña = request.POST.get('contraseña')
    empleado = Empleado.objects.filter(Q (Rut = usuario))
    verificar = User.objects.filter(Q(username=usuario))
    if usuario == "root" and contraseña == "proyectosentte":
        return HttpResponseRedirect("adminInicio")
    else:
        if usuario:
            cuentausuario = User.objects.filter(Q (username = usuario))
            cuentacontra = User.objects.filter(Q (password = contraseña))
            if cuentausuario and cuentacontra:
                return HttpResponseRedirect("evaluadorInicio")
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html")

# ----------------------------------  Administrador ---------------------------------.
@login_required
def admin_inicio(request):
    return render(request, "admin/adminInicio.html")

# -- ------------Acciones Claves----------------.
def admin_acciones(request):
    accioneclaves = AccionClave.objects.all().order_by('id') 
    contexto = {
        'accionclaves':accioneclaves,
        'form': AccionesForm()
    }
    if request.method == 'POST':
        formulario = AccionesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con exito" )
            return HttpResponseRedirect("adminAcciones")
        else:
            messages.warning(request, "Se verifico y no se pudo guardar la informacion")
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
    cargos = Cargo.objects.all().order_by('NombreCargo')
    contexto = {
        'cargos':cargos,
        'form': CargoForm()
    }
    if request.method == 'POST':
        formulario = CargoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con exito" )
            return HttpResponseRedirect("adminCargos")
        else:
            messages.warning(request, "Se verifico y no se pudo guardar la informacion")
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
    competencias = Competencia.objects.all().order_by('NombreCompetencia')
    contexto1 = {
        'competencias': competencias,
        'form': CompetenciaForm()
    }
    if request.method == 'POST':
        formulario = CompetenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con exito" )
            return HttpResponseRedirect("adminCompetencias")
        else:
            messages.warning(request, "Se verifico y no se pudo guardar la informacion")
            return HttpResponseRedirect("adminCompetencias")
    return render(request, "admin/adminCompetencias.html", contexto1)

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
    gerencias = Gerencia.objects.all().order_by('NombreGerencia')
    contexto = {
        'gerencias': gerencias,
        'form': GerenciaForm()
    }
    if request.method == 'POST':
        formulario = GerenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con exito" )
            return HttpResponseRedirect("adminGerencias")
        else:
            messages.warning(request, "Se verifico y no se pudo guardar la informacion")
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
    subgerencias = SubGerencia.objects.all().order_by('NombreSubgerencia')
    contexto = {
        'subgerencias': subgerencias,
        'form': SubgerenciaForm()
    }
    if request.method == 'POST':
        formulario = SubgerenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con exito" )
            return HttpResponseRedirect("adminSubgerencias")
        else:
            messages.warning(request, "Se verifico y no se pudo guardar la informacion")
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
    empleados = Empleado.objects.all().order_by('Rut')
    contexto = {
        'empleados': empleados,
        'form': EmpleadoForm(), 
        'form1': PerfilRolForm(),
        'form2': PerilForm(),
        'form3': UserForm()
    }
    if request.method == 'POST':
        formularioPerfil = PerilForm(request.POST)
        form = UserForm(request.POST)
        formEmpleado = EmpleadoForm(request.POST)
        formPerfilrol = PerfilRolForm(request.POST)

        if form.is_valid() and formularioPerfil.is_valid() and formPerfilrol.is_valid() and formEmpleado.is_valid():
            
            usuario = formEmpleado.save(commit=False)
            usuario.user = form.save()
            usuario.save()
            rolempleado = formPerfilrol.save(commit=False)
            rolempleado.IdEmpleado = formEmpleado.save()
            rolempleado.save()
            formularioPerfil.save()

            messages.success(request, "Guardado con exito" )
            return HttpResponseRedirect("adminUsuarios")
        else:
            messages.warning(request, "Se verifico y no se pudo guardar la informacion")
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