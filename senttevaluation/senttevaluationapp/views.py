from functools import reduce
from django import http
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import query_utils
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
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
    if usuario == "root" and contraseña == "proyectosentte":
        return HttpResponseRedirect("home")
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
    data = {
        'page': 'Inicio',
    }

    return render(request, "admin/home.html", data)

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

    data = {
        'entity':accioneclaves,
        'paginator': paginator,
        'titulo': 'Acciones',
        'page': 'Acciones',
    }

    return render(request, "admin/adminAcciones.html", data)

@login_required
def agregar_acciones(request):
    data = {
        'form': AccionesForm(),
        'titulo': 'Acción',
        'page': 'Acciones',
    }

    if request.method == 'POST':
        formulario = AccionesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardada con éxito" )
            return HttpResponseRedirect("adminAcciones")
        else:
            data["form"] = formulario
    return render(request, "admin/adminAgregarAcciones.html", data)

@login_required
def editar_acciones(request, id):
    acciones = get_object_or_404(AccionClave, id=id)

    data = {
        'form':  AccionesForm(instance=acciones),
        'page': 'Acciones',
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
    return redirect(to="adminAcciones")

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

    data = {
        'entity':cargos,
        'paginator': paginator,
        'titulo': 'Cargo',
        'page': 'Cargos',
    }

    return render(request,"admin/adminCargos.html", data)

@login_required
def agregar_cargos(request):
    data = {
        'form': CargoForm(),
        'titulo': 'Cargo',
        'page': 'Cargos',
    }

    if request.method == 'POST':
        formulario = CargoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con éxito" )
            return HttpResponseRedirect("adminCargos")
        else:
            data["form"] = formulario
    return render(request,"admin/adminAgregarCargos.html", data)

@login_required
def editar_cargos(request, id):
    cargos = get_object_or_404(Cargo, id=id)

    data = {
        'form':  CargoForm(instance=cargos),
        'page': 'Cargos',
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

# -- ------------ Perfiles ----------------.
@login_required
def admin_perfil(request):
    perfils = Perfil.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(perfils, 10)
        perfils = paginator.page(page)
    except:
        Http404

    data = {
        'perfils':listarperfil(),
        'entity':perfils,
        'paginator': paginator,
        'titulo': 'Perfil',
        'page': 'Perfil',
    }

    return render(request,"admin/adminPerfil.html", data)

def listarperfil():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_perfil", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

@login_required
def agregar_perfil(request):
    data = {
        'form': PerfilForm(),
        'titulo': 'Perfil',
        'page': 'Perfil',
    }

    if request.method == 'POST':
        formulario = PerfilForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado con éxito" )
            return HttpResponseRedirect("adminPerfil")
        else:
            data["form"] = formulario
    return render(request,"admin/adminAgregarPerfil.html", data)


@login_required
def editar_perfil(request, id):
    perfils = get_object_or_404(Perfil, id=id)

    data = {
        'form':  PerfilForm(instance=perfils),
        'page': 'Perfil',
    }

    if request.method == 'POST':
        formulario = PerfilForm(data=request.POST, instance=perfils)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado con éxito" )
            return redirect(to="adminPerfil")
        else:
            data["form"] = formulario
    return render(request, "admin/adminModificarPerfil.html", data)

@login_required
def eliminar_perfil(request, id):
    perfils = get_object_or_404(Perfil, id=id)
    perfils.delete()
    messages.success(request, "Eliminado con éxito" )
    return redirect(to="adminPerfil")

# -----------------------------------------------------------------------------------------------.

# -- ------------ Competencias ----------------.
@login_required
def admin_competencias(request):
    competencias = Competencia.objects.all().order_by('NombreCompetencia')
    perfil = Perfil.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(competencias, 10)
        competencias = paginator.page(page)
    except:
        Http404

    data = {
        'entity': competencias,
        'perfil':perfil,
        'paginator':paginator,
        'titulo':'Competencia',
        'page':'Competencias',
    }
    return render(request, "admin/adminCompetencias.html", data)

@login_required
def agregar_competencias(request):
    data = {
        'form':CompetenciaForm(),
        'titulo':'Competencia',
        'page':'Competencias',
    }

    if request.method == 'POST':
        formulario = CompetenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardada con éxito" )
            return HttpResponseRedirect("adminCompetencias")
        else:
            data["form"] = formulario
    return render(request, "admin/adminAgregarCompetencias.html", data)

@login_required
def editar_competencias(request, id):
    competencias = get_object_or_404(Competencia, id=id)

    data = {
        'form':  CompetenciaForm(instance=competencias),
        'page': 'Competencias',
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

    data = {
        'gerencias':listargerencia(),
        'entity': gerencias,
        'paginator': paginator,
        'titulo': 'Gerencia',
        'page': 'Gerencias',
    }

    return render(request, "admin/adminGerencias.html", data)

def listargerencia():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_gerencia", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

@login_required
def agregar_gerencias(request):
    data = {
        'form': GerenciaForm(),
        'titulo': 'Gerencia',
        'page': 'Gerencias',
    }

    if request.method == 'POST':
        formulario = GerenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardada con éxito" )
            return HttpResponseRedirect("adminGerencias")
        else:
            data["form"] = formulario
    return render(request, "admin/adminAgregarGerencias.html", data)

@login_required
def editar_gerencias(request, id):
    gerencias = get_object_or_404(Gerencia, id=id)

    data = {
        'form':  GerenciaForm(instance=gerencias),
        'page': 'Gerencias',
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

    data = {
        'entity': subgerencias,
        'paginator': paginator,
        'titulo': 'Subgerencia',
        'page': 'Subgerencias',
    }

    return render(request, "admin/adminSubgerencias.html", data)

@login_required
def agregar_subgerencias(request):
    data = {
        'form': SubgerenciaForm(),
        'titulo': 'Subgerencia',
        'page': 'Subgerencias',
    }

    if request.method == 'POST':
        formulario = SubgerenciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardada con éxito" )
            return HttpResponseRedirect("adminSubgerencias")
        else:
            data["form"] = formulario
    return render(request, "admin/adminAgregarSubgerencias.html", data)

@login_required
def editar_subgerencia(request, id):
    subgerencias = get_object_or_404(SubGerencia, id=id)

    data = {
        'form':  SubgerenciaForm(instance=subgerencias),
        'page': 'Subgerencias',
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
# -- ------------ Area ----------------.

@login_required
def admin_areas(request):
    areas  = Area.objects.all().order_by('NombreArea')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(areas, 10)
        areas = paginator.page(page)
    except:
        Http404

    data = {
        'entity': areas,
        'paginator': paginator,
        'titulo': 'Áreas',
        'page': 'Áreas',
    }

    return render(request, "admin/adminArea.html", data)

@login_required
def agregar_areas(request):
    data = {
        'form': AreaFrom(),
        'titulo': 'Areas',
        'page': 'Areas',
    }

    if request.method == 'POST':
        formulario = AreaFrom(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardada con éxito" )
            return HttpResponseRedirect("adminArea")
        else:
            data["form"] = formulario
    return render(request, "admin/adminAgregarArea.html", data)

@login_required
def editar_area(request, id):
    areas = get_object_or_404(Area, id=id)

    data = {
        'form':  AreaFrom(instance=areas),
        'page': 'Areas',
    }

    if request.method == 'POST':
        formulario = AreaFrom(data=request.POST, instance=areas)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editada con éxito" )
            return redirect(to="adminArea")
        else:
            data["form"] = formulario
    return render(request, "admin/adminAreaModificar.html", data)

@login_required
def eliminar_area(request, id):
    areas = get_object_or_404(Area, id=id)
    areas.delete()
    messages.success(request, "Eliminada con éxito" )
    return redirect(to="adminArea")

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

    data = {
        'entity': empleados,
        'paginator': paginator,
        'titulo': 'Empleado',
        'page': 'Usuarios',
    }

    return render(request, "admin/adminUsuarios.html", data)

@login_required
def agregar_usuario(request):
    data = {
        'form': EmpleadoForm(),
        'form1': PerfilRolForm(),
        'form3': UserForm(),
        'titulo': 'Empleado',
        'page': 'Usuarios',
    }

    if request.method == 'POST':
        form = UserForm(request.POST)
        formEmpleado = EmpleadoForm(request.POST, request.FILES)
        formPerfilrol = PerfilRolForm(request.POST)
        formEvaluacion = EvaluacionForm()
        if form.is_valid() and formPerfilrol.is_valid() and formEmpleado.is_valid():
            usuario = formEmpleado.save(commit=False)
            usuario.user = form.save()
            usuario.save()
            rolempleado = formPerfilrol.save(commit=False)
            rolempleado.IdEmpleado = formEmpleado.save()
            rolempleado.save()
            cuentausuario = form.save()
            evaluaciones = formEvaluacion.save(commit=False)
            evaluaciones.Estado = "Pendiente"
            evaluaciones.Fase = "Planificacion"
            evaluaciones.IdEmpleado = formEmpleado.save()
            evaluaciones.save()

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
            data["form"] = formEmpleado,
            data["form1"] = formPerfilrol,
            data["form3"] = form
    return render(request, "admin/adminAgregarUsuarios.html", data)


@login_required
def editar_usuario(request, id):
    empleados = get_object_or_404(Empleado, id=id)

    data = {
        'form':  EmpleadoForm(instance=empleados),
        'page': 'Usuarios',
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, files=request.FILES, instance=empleados)
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
    usuario = get_object_or_404(User, username=empleados.user)
    usuario.delete()
    empleados.delete()
    messages.success(request, "Eliminado con éxito" )
    return redirect(to="adminUsuarios")

# -----------------------------------------------------------------------------------------------.
# ----------------------------------  Indicadores(graficos)  ---------------------------------.

@login_required
def admin_indicadores(request):
    evplanificacion = Evaluacion.objects.filter(Fase='Planificacion').count()
    evevaluacion = Evaluacion.objects.filter(Fase='Evaluacion').count()
    evevaluacionfinal = Evaluacion.objects.filter(Fase='FinalEv').count()
    totalevaluacion = Evaluacion.objects.all().count()

    data = {
        'page':'Indicadores',
        "evplanificacion":evplanificacion,
        'evevaluacion':evevaluacion,
        'evevaluacionfinal':evevaluacionfinal,
        'totalevaluacion':totalevaluacion,
    }  

    return render(request, "admin/adminIndicadores.html", data)

def get_data(request, *args, **kwargs):
    data= {
        "sales":100,
        "customers": 10
    }

    return JsonResponse(data)

# -----------------------------------------------------------------------------------------------.
@login_required
def admin_ayuda(request):
    data = {
        'page': 'Ayuda',
    }

    return render(request, "admin/adminAyuda.html", data)

# -----------------------------------------------------------------------------------------------.

# ----------------------------------  Evaluador ---------------------------------.
@login_required
def evaluador_inicio(request):
    data = {
        'page': 'Inicio',
    }

    return render(request, "evaluador/evaluadorInicio.html", data)

@login_required
def evaluador_evaluacion(request):
    empleados = Empleado.objects.all()
    evaluacion = Evaluacion.objects.all()
    perfilrol = PerfilRol.objects.all()

    data = {
        'empleados':empleados,
        'evaluacion':evaluacion,
        'perfilrol':perfilrol,
        'page': 'Evaluación',
        'titulo': 'Formulario',
    }

    return render(request, "evaluador/evaluadorEvaluacion.html", data)

@login_required
def evaluador_autovaluacion(request, id):
    evaluaciones = get_object_or_404(Evaluacion, id=id)
    competencias = Competencia.objects.all()
    accionclaves = AccionClave.objects.all()
    planaccion = PlanAccion.objects.all()
    
    data = {
        'empleados': Empleado.objects.get(Nombre = evaluaciones.IdEmpleado.Nombre),
        'competencias':competencias,
        'accionclaves':accionclaves,
        'planaccion': planaccion,
        'evaluacion': Evaluacion.objects.get(id = evaluaciones.id),
        'page': 'AutoEvaluacion', 
        'form': EvaluacionForm(instance=evaluaciones),
    }

    if request.method == 'POST':
        formulario = EvaluacionForm(data=request.POST, instance=evaluaciones)
        if formulario.is_valid():
            form = formulario.cleaned_data.get("Verificar")
            evaluacionid = Evaluacion.objects.get(id = id)
            evaluacionid.Verificar = form
            if evaluacionid.Verificar == 1:
                evaluacionid.Estado = "Pendiente"
                evaluacionid.Fase = "Evaluacion"
                evaluacionid.save()
                messages.success(request,'Guardada la evaluación')   
                return redirect(to="evaluadorEvaluacion")
            else:
                  return redirect(to="evaluadorEvaluacion")
    return render(request, "evaluador/evaluadorAutovaluacion.html",data)

@login_required
def evaluador_autovaluacion2(request, id):
    evaluaciones = get_object_or_404(Evaluacion, id=id)
    competencias = Competencia.objects.all()
    accionclaves = AccionClave.objects.all()
    
    data = {
        'empleados': Empleado.objects.get(Nombre = evaluaciones.IdEmpleado.Nombre),
        'competencias':competencias,
        'accionclaves':accionclaves,
        'page': 'Formulario', 
        'form': EvaluacionForm(instance=evaluaciones),
    }

    if request.method == 'POST':
        formulario = EvaluacionForm(data=request.POST, instance=evaluaciones)
        if formulario.is_valid():
            form2 = formulario.cleaned_data.get("AutoEvaluacion")
            evaluacionid = Evaluacion.objects.get(id = id)
            evaluacionid.AutoEvaluacion = form2
            evaluacionid.Estado = "Guardado"
            evaluacionid.Fase = "Evaluacion"
            evaluacionid.save()
            messages.success(request,'Guardada la evaluación')   
            return redirect(to="evaluadorEvaluacion")
    return render(request, "evaluador/evaluadorAutovaluacion2.html",data)


@login_required
def evaluador_ayuda(request):
    data = {
        'page': 'Ayuda',
    }

    return render(request, "evaluador/evaluadorAyuda.html", data)

@login_required
def evaluador_formulario(request, id):
    evaluaciones = get_object_or_404(Evaluacion, id=id)
    competencias = Competencia.objects.all()
    accionclaves = AccionClave.objects.all()
    
    data = {
        'empleados': Empleado.objects.get(Nombre = evaluaciones.IdEmpleado.Nombre),
        'competencias':competencias,
        'accionclaves':accionclaves,
        'page': 'Formulario', 
        'form': PlanAccionForm(),
        'form2': EvaluacionForm()
    }

    if request.method == 'POST':
        formulario = PlanAccionForm(request.POST)
        if formulario.is_valid():
            evaluacionid = Evaluacion.objects.get(id = id)
            plan = formulario.save(commit=False)
            plan.IdEvaluacion = evaluacionid
            plan.save()
            evaluacionid.Estado = "Guardado"
            evaluacionid.save()
            messages.success(request,'Guardada la evaluación')   
            return redirect(to="evaluadorEvaluacion")
    return render(request, "evaluador/evaluadorFormulario.html",data)

@login_required
def evaluador_formulario2(request, id):
    evaluaciones = get_object_or_404(Evaluacion, id=id)
    competencias = Competencia.objects.all()
    accionclaves = AccionClave.objects.all()
    
    data = {
        'empleados': Empleado.objects.get(Nombre = evaluaciones.IdEmpleado.Nombre),
        'competencias':competencias,
        'accionclaves':accionclaves,
        'page': 'Formulario',
        'form': EvaluacionForm(instance=evaluaciones),
    }

    if request.method == 'POST':
        formulario = EvaluacionForm(data=request.POST, instance=evaluaciones)
        if formulario.is_valid():
            form = formulario.cleaned_data.get("ComentarioEvaluador")
            form2 = formulario.cleaned_data.get("Calificacion")
            evaluacionid = Evaluacion.objects.get(id = id)
            evaluacionid.ComentarioEvaluador = form
            evaluacionid.Calificacion = form2
            evaluacionid.Estado = "Pendiente"
            evaluacionid.Fase = "FinalEv"
            evaluacionid.save()
            messages.success(request,'Guardada la evaluación')   
            return redirect(to="evaluadorEvaluacion")
    return render(request, "evaluador/evaluadorFormulario2.html", data)

@login_required
def evaluador_formulario3(request, id):
    evaluaciones = get_object_or_404(Evaluacion, id=id)
    competencias = Competencia.objects.all()
    accionclaves = AccionClave.objects.all()
    
    data = {
        'empleados': Empleado.objects.get(Nombre = evaluaciones.IdEmpleado.Nombre),
        'competencias':competencias,
        'accionclaves':accionclaves,
        'page': 'Formulario', 
        'form': EvaluacionForm(instance=evaluaciones),
        'evaluacion': Evaluacion.objects.get(id = evaluaciones.id),
    }

    if request.method == 'POST':
        formulario = EvaluacionForm(data=request.POST, instance=evaluaciones)
        if formulario.is_valid():
            form = formulario.cleaned_data.get("AutoEvaluacion")
            form2 = formulario.cleaned_data.get("Calificacion")
            evaluacionid = Evaluacion.objects.get(id = id)
            evaluacionid.AutoEvaluacion = form
            evaluacionid.Calificacion = form2
            evaluacionid.Estado = "Finalizado"
            evaluacionid.save()
            messages.success(request,'Guardada la evaluación')
            return redirect(to="evaluadorEvaluacion")
    return render(request, "evaluador/evaluadorFormulario3.html", data)

# ----------------------------------  Colaborador ---------------------------------.
@login_required
def colaborador_inicio(request):
    data = {
        'page': 'Inicio',
    }

    return render(request, "colaborador/colaboradorInicio.html", data)

@login_required
def colaborador_ayuda(request):
    data = {
        'page': 'Ayuda',
    }

    return render(request, "colaborador/colaboradorAyuda.html", data)

@login_required
def colaborador_autovaluacion(request):
    data = {
        'page': 'Autoevaluación',
    }

    return render(request, "colaborador/colaboradorAutovaluacion.html", data)

# ----------------------------------  Calibrador ---------------------------------.
@login_required
def calibrador_inicio(request):
    data = {
        'page': 'Inicio',
    }

    return render(request, "calibrador/calibradorInicio.html", data)

@login_required
def calibrador_ayuda(request):
    data = {
        'page': 'Ayuda',
    }

    return render(request, "calibrador/calibradorAyuda.html", data)

@login_required
def calibrador_evaluaciones(request):
    data = {
        'page': 'Evaluaciones',
    }

    return render(request, "calibrador/calibradorEvaluaciones.html", data)