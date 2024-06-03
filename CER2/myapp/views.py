from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Create your views here.
def base(request):
    datos= {}
    proyectos= []
    for proyecto in Proyecto.objects.all():
        proyectos.append(proyecto)
    datos["proyectos"] = proyectos
    return render(request,'myapp/base.html', datos)

def crearFormulario(request):
    ##CREAR FORMULARIO##
    nombre = request.POST.get("nombre")
    estudiante = request.POST.get("estudiante")
    tema = request.POST.get("tema")
    profesor = request.POST.get("profesor")

    nuevo_proyecto = Proyecto(nombreProyecto=nombre, estudiante=estudiante, tema=tema, profesor=profesor)
    nuevo_proyecto.save()
    return redirect("base")

def index(request):

    respuestaSegmento = request.GET.get('Segmento')
    mostrar = False
    for u in UsuarioSegmento.objects.all():
        if u.usuario == request.user:
            segmento_usuario = u.tipo_segmento
            if (segmento_usuario in ["P"]):
                mostrar = True

    Usuario = request.user

    segmentos={"Estudiante":'E',
                "Profesor":'P',
         }
    
    data={
        "Segmentos":segmentos,
        "respuestaSegmento":respuestaSegmento,
        "Usuario":Usuario,
        "mostrar":mostrar,
    }
    return redirect("base", data)

def login(request):
    users = []
    nombre = request.GET.get('usuario')
    contraseña = request.GET.get('contraseña')
    logeado = 1
    if (nombre != None) and (contraseña!=None):
        logeado = 3

    for u in User.objects.all():
        users.append((u.username,u.password))

    for usuario in users:
        if usuario[0] == nombre:
            if check_password(contraseña,usuario[1]):
                logeado = 2
    data={
        "Usuarios":users,
        "con":contraseña,
        "nombre":nombre,
        "si":logeado
    }
    return redirect("base", data)