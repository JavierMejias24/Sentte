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
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
# ----------------------------------  Login ---------------------------------.
def login(request):

    usuario = request.POST.get('name')
    contraseña = request.POST.get('contraseña')
    empleado = Empleado.objects.filter(Q (Rut = usuario))
    verificar = User.objects.filter(Q (username=usuario))
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
@login_required
def admin_acciones(request):
    accioneclaves = AccionClave.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(accioneclaves, 10)
        accioneclaves = paginator.page(page)
    except:
        Http404

    contexto = {
        'entity':accioneclaves,
        'paginator': paginator,
        'titulo': 'Cargo'
    }
    return render(request, "admin/adminAcciones.html", contexto)

@login_required
def agregar_acciones(request):
    contexto = {
        'form': AccionesForm(),
        'titulo': 'Acción'
    }
    if request.method == 'POST':
        formulario = AccionesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardada con éxito" )
            return HttpResponseRedirect("adminAcciones")
        else:
            contexto["form"] = formulario
    return render(request, "admin/adminAgregarAcciones.html", contexto)

@login_required
def editar_acciones(request, id):
    acciones = get_object_or_404(AccionClave, id=id)
    data = {
        'form':  AccionesForm(instance=acciones)
    }
    if request.method == 'POST':
        formulario = AccionesForm(data=request.POST, instance=acciones)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editada con éxito" )
            return redirect(to="adminAcciones")
        else:
            data["form"] = formulario
    return render(request, "admin/adminAccionesModificar.html", data)

@login_required
def eliminar_acciones(request, id):
    acciones = get_object_or_404(AccionClave, id=id)
    acciones.delete()
    messages.success(request, "Eliminada con éxito" )
    return redirect(to='adminAcciones')
# -----------------------------------------------------------------------------------------------.

# -- ------------ Cargos ----------------.
@login_required
def admin_cargos(request):
    cargos = Cargo.objects.all().order_by('NombreCargo')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(cargos, 10)
        cargos = paginator.page(page)
    except:
        Http404

    contexto = {
        'entity':cargos,
        'paginator': paginator,
        'titulo': 'Cargo'
    }
    return render(request,"admin/adminCargos.html", contexto)

@login_required
def agregar_cargos(request):
    contexto = {
        'form': CargoForm(),
        'titulo': 'Cargo'
    }

    if request.method == 'POST':
        formulario = CargoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con éxito" )
            return HttpResponseRedirect("adminCargos")
        else:
            contexto["form"] = formulario
    return render(request,"admin/adminAgregarCargos.html", contexto)

@login_required
def editar_cargos(request, id):
    cargos = get_object_or_404(Cargo, id=id)
    data = {
        'form':  CargoForm(instance=cargos)
    }
    if request.method == 'POST':
        formulario = CargoForm(data=request.POST, instance=cargos)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado con éxito" )
            return redirect(to="adminCargos")
        else:
            data["form"] = formulario
    return render(request, "admin/adminCargosModificar.html", data)

@login_required
def eliminar_cargos(request, id):
    cargos = get_object_or_404(Cargo, id=id)
    cargos.delete()
    messages.success(request, "Eliminado con éxito" )
    return redirect(to="adminCargos")

# -----------------------------------------------------------------------------------------------.

# -- ------------ Competencias ----------------.
@login_required
def admin_competencias(request):
    competencias = Competencia.objects.all().order_by('NombreCompetencia')
    perfilcomp = PerfilComp.objects.all()
    perfil = Perfil.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(competencias, 10)
        competencias = paginator.page(page)
    except:
        Http404

    contexto1 = {
        'entity': competencias,
        'perfilcomp':perfilcomp,
        'perfil':perfil,
        'paginator': paginator,
        'titulo': 'Competencia'
    }
    return render(request, "admin/adminCompetencias.html", contexto1)

@login_required
def agregar_competencias(request):
    contexto1 = {
        
        'form': CompetenciaForm(),
        'titulo': 'Competencia'
    }
    if request.method == 'POST':
        formulario = CompetenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardada con éxito" )
            return HttpResponseRedirect("adminCompetencias")
        else:
            contexto1["form"] = formulario
    return render(request, "admin/adminAgregarCompetencias.html", contexto1)

@login_required
def editar_competencias(request, id):
    competencias = get_object_or_404(Competencia, id=id)
    data = {
        'form':  CompetenciaForm(instance=competencias)
    }
    if request.method == 'POST':
        formulario = CompetenciaForm(data=request.POST, instance=competencias)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editada con éxito" )
            return redirect(to="adminCompetencias")
        else:
            data["form"] = formulario
    return render(request, "admin/adminCompetenciasModificar.html", data)

@login_required
def eliminar_competencias(request, id):
    competencias = get_object_or_404(Competencia, id=id)
    competencias.delete()
    messages.success(request, "Eliminada con éxito" )
    return redirect(to="adminCompetencias")

# -----------------------------------------------------------------------------------------------.

# -- ------------ Gerencias ----------------.
@login_required
def admin_gerencias(request):
    gerencias = Gerencia.objects.all().order_by('NombreGerencia')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(gerencias, 10)
        gerencias = paginator.page(page)
    except:
        Http404

    contexto = {
        'entity': gerencias,
        'paginator': paginator,
        'titulo': 'Gerencia'
    }
    return render(request, "admin/adminGerencias.html", contexto)

@login_required
def agregar_gerencias(request):
    contexto = {
        'form': GerenciaForm(),
        'titulo': 'Gerencia'
    }
    if request.method == 'POST':
        formulario = GerenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardada con éxito" )
            return HttpResponseRedirect("adminGerencias")
        else:
            contexto["form"] = formulario
    return render(request, "admin/adminAgregarGerencias.html", contexto)

@login_required
def editar_gerencias(request, id):
    gerencias = get_object_or_404(Gerencia, id=id)
    data = {
        'form':  GerenciaForm(instance=gerencias)
    }
    if request.method == 'POST':
        formulario = GerenciaForm(data=request.POST, instance=gerencias)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editada con éxito" )
            return redirect(to="adminGerencias")
        else:
            data["form"] = formulario
    return render(request, "admin/adminGerenciasModificar.html", data)

@login_required
def eliminar_gerencias(request, id):
    gerencias = get_object_or_404(Gerencia, id=id)
    gerencias.delete()
    messages.success(request, "Eliminada con éxito" )
    return redirect(to="adminGerencias")
# -----------------------------------------------------------------------------------------------.

# -- ------------ Sub-gerencias ----------------.
@login_required
def admin_subgerencias(request):
    subgerencias = SubGerencia.objects.all().order_by('NombreSubgerencia')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(subgerencias, 10)
        subgerencias = paginator.page(page)
    except:
        Http404

    contexto = {
        'entity': subgerencias,
        'paginator': paginator,
        'titulo': 'Subgerencia'
    }
    return render(request, "admin/adminSubgerencias.html", contexto)

@login_required
def agregar_subgerencias(request):

    contexto = {
        'form': SubgerenciaForm(),
        'titulo': 'Subgerencia'
    }

    if request.method == 'POST':
        formulario = SubgerenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardada con éxito" )
            return HttpResponseRedirect("adminSubgerencias")
        else:
            contexto["form"] = formulario
    return render(request, "admin/adminAgregarSubgerencias.html", contexto)


@login_required
def editar_subgerencia(request, id):
    subgerencias = get_object_or_404(SubGerencia, id=id)
    data = {
        'form':  SubgerenciaForm(instance=subgerencias)
    }
    if request.method == 'POST':
        formulario = SubgerenciaForm(data=request.POST, instance=subgerencias)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editada con éxito" )
            return redirect(to="adminSubgerencias")
        else:
            data["form"] = formulario
    return render(request, "admin/adminSubgerenciasModificar.html", data)

@login_required
def eliminar_subgerencia(request, id):
    subgerencias = get_object_or_404(SubGerencia, id=id)
    subgerencias.delete()
    messages.success(request, "Eliminada con éxito" )
    return redirect(to="adminSubgerencias")
# -----------------------------------------------------------------------------------------------.

# -- ------------ Empleado ----------------.
@login_required
def admin_usuarios(request):
    empleados = Empleado.objects.all().order_by('Rut')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(empleados, 10)
        empleados = paginator.page(page)
    except:
        Http404

    contexto = {
        'entity': empleados,
        'paginator': paginator,
        'titulo': 'Empleado'
    }
    return render(request, "admin/adminUsuarios.html",contexto)

@login_required
def agregar_usuario(request):

    contexto = {
        'form': EmpleadoForm(),
        'form1': PerfilRolForm(),
        'form3': UserForm(),
        'titulo': 'Empleado'
    }

    if request.method == 'POST':
        
        form = UserForm(request.POST)
        formEmpleado = EmpleadoForm(request.POST)
        formPerfilrol = PerfilRolForm(request.POST)

        if form.is_valid() and formPerfilrol.is_valid() and formEmpleado.is_valid():
            
            usuario = formEmpleado.save(commit=False)
            usuario.user = form.save()
            usuario.save()
            rolempleado = formPerfilrol.save(commit=False)
            rolempleado.IdEmpleado = formEmpleado.save()
            rolempleado.save()
            
            cuentausuario = form.save()

            #Permiso Cargos
            content_type = ContentType.objects.get_for_model(Cargo)
            permission1 = Permission.objects.get( codename = 'view_cargo', content_type = content_type)
            cuentausuario.user_permissions.add(permission1)

            #Permiso Sub Gerencia
            content_type1 = ContentType.objects.get_for_model(SubGerencia)
            permission2 = Permission.objects.get( codename = 'view_subgerencia', content_type = content_type1)
            cuentausuario.user_permissions.add(permission2)

            #Permiso Accion Clave
            content_type2 = ContentType.objects.get_for_model(AccionClave)
            permission3 = Permission.objects.get( codename = 'view_accionclave', content_type = content_type2)
            cuentausuario.user_permissions.add(permission3)

            #Permiso Area
            content_type3 = ContentType.objects.get_for_model(Area)
            permission4 = Permission.objects.get( codename = 'view_area', content_type = content_type3)
            cuentausuario.user_permissions.add(permission4)

            #Permiso Competencia
            content_type4 = ContentType.objects.get_for_model(Competencia)
            permission5 = Permission.objects.get( codename = 'view_competencia', content_type = content_type4)
            cuentausuario.user_permissions.add(permission5)

            #Permiso Detalle Evaluacion
            content_type5 = ContentType.objects.get_for_model(DetalleEv)
            permission6 = Permission.objects.get( codename = 'view_detalleev', content_type = content_type5)
            cuentausuario.user_permissions.add(permission6)

            #Permiso Empleado
            content_type6 = ContentType.objects.get_for_model(Empleado)
            permission7 = Permission.objects.get( codename = 'view_empleado', content_type = content_type6)
            cuentausuario.user_permissions.add(permission7)

            #Permiso Evaluacion
            content_type7 = ContentType.objects.get_for_model(Evaluacion)
            permission8 = Permission.objects.get( codename = 'view_evaluacion', content_type = content_type7)
            cuentausuario.user_permissions.add(permission8)

            #Permiso Gerencia
            content_type8 = ContentType.objects.get_for_model(Gerencia)
            permission9 = Permission.objects.get( codename = 'view_gerencia', content_type = content_type8)
            cuentausuario.user_permissions.add(permission9)

            #Permiso Perfil
            content_type9 = ContentType.objects.get_for_model(Perfil)
            permission10 = Permission.objects.get( codename = 'view_perfil', content_type = content_type9)
            cuentausuario.user_permissions.add(permission10)

            #Permiso Perfil Rol
            content_type10 = ContentType.objects.get_for_model(PerfilRol)
            permission11 = Permission.objects.get( codename = 'view_perfilrol', content_type = content_type10)
            cuentausuario.user_permissions.add(permission11)

            #Permiso Plan accion
            content_type11 = ContentType.objects.get_for_model(PlanAccion)
            permission12 = Permission.objects.get( codename = 'view_planaccion', content_type = content_type11)
            cuentausuario.user_permissions.add(permission12)
            
            messages.success(request, "Guardado con éxito" )
            return HttpResponseRedirect("adminUsuarios")
        else:
            contexto["form"] = formEmpleado,
            contexto["form1"] = formPerfilrol,
            contexto["form3"] = form
    return render(request, "admin/adminAgregarUsuarios.html",contexto)


@login_required
def editar_usuario(request, id):
    empleados = get_object_or_404(Empleado, id=id)
    data = {
        'form':  EmpleadoForm(instance=empleados)
    }
    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleados)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado con éxito" )
            return redirect(to="adminUsuarios")
        else:
            data["form"] = formulario
    return render(request, "admin/adminUsuariosModificar.html", data)

@login_required
def eliminar_usuario(request, id):
    empleados = get_object_or_404(Empleado, id=id)
    empleados.delete()
    messages.success(request, "Eliminado con éxito" )
    return redirect(to="adminUsuarios")

# -----------------------------------------------------------------------------------------------.

@login_required
def admin_ayuda(request):
    return render(request, "admin/adminAyuda.html")

# -----------------------------------------------------------------------------------------------.

# ----------------------------------  Evaluador ---------------------------------.
@login_required
def evaluador_inicio(request):
    return render(request, "evaluador/evaluadorInicio.html")

@login_required
def evaluador_evaluacion(request):
    empleados = Empleado.objects.all()
    
    contexto = {
        'empleados':empleados,
    }
    return render(request, "evaluador/evaluadorEvaluacion.html", contexto)

@login_required
def evaluador_autovaluacion(request):
    return render(request, "evaluador/evaluadorAutovaluacion.html")

@login_required
def evaluador_ayuda(request):
    return render(request, "evaluador/evaluadorAyuda.html")

@login_required
def evaluador_formulario(request, id):
    empleados = get_object_or_404(Empleado, id=id)
    competencias = Competencia.objects.all()
    accionclaves = AccionClave.objects.all()
    data = {
        'empleados': Empleado.objects.get(Nombre = empleados),
        'competencias':competencias,
        'accionclaves':accionclaves,
    }
    
    return render(request, "evaluador/evaluadorFormulario.html", data)

# ----------------------------------  Colaborador ---------------------------------.
@login_required
def colaborador_inicio(request):
    return render(request, "colaborador/colaboradorInicio.html")

@login_required
def colaborador_ayuda(request):
    return render(request, "colaborador/colaboradorAyuda.html")

@login_required
def colaborador_autovaluacion(request):
    return render(request, "colaborador/colaboradorAutovaluacion.html")

# ----------------------------------  Calibrador ---------------------------------.
@login_required
def calibrador_inicio(request):
    return render(request, "calibrador/calibradorInicio.html")

@login_required
def calibrador_ayuda(request):
    return render(request, "calibrador/calibradorAyuda.html")

@login_required
def calibrador_evaluaciones(request):
    return render(request, "calibrador/calibradorEvaluaciones.html")