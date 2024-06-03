from .models import *
from django.shortcuts import render

# Create your views here.
def base(request):
    datos = {}
    proyectos = Proyecto.objects.all()
    nombres = []
    for proyecto in proyectos:
        nombres.append(proyecto.nombreProyecto)
    datos["nombreProyecto"] = nombres
    return render(request,'myapp/base.html', datos)