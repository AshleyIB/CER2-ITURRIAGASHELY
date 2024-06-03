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



def login(request):
    tipo_usuario = "invitado"
    proyectos= []
    users = Usuario.objects.all()
    nombre = request.POST.get('usuario')
    contraseña = request.POST.get('contraseña')
    logeado = 1
    if (nombre != None) and (contraseña!=None):
        logeado = 3

    for usuario in users:
        if usuario.nombre == nombre:
            if contraseña == usuario.contrasena:
                tipo_usuario = usuario.tipo_usuario
                logeado = 2

    
    for proyecto in Proyecto.objects.all():
        proyectos.append(proyecto)
    

    data={
        "Usuarios":users,
        "con":contraseña,
        "nombre":nombre,
        "si":logeado,
        "tipo": tipo_usuario,
        "proyectos": proyectos,
    }
    return render(request,'myapp/base.html', data)