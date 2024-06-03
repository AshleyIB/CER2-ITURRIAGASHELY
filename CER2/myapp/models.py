from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TIPO_USUARIO = (
    ("E","Estudiante"),
    ("P","Profesor")
)

class Proyecto(models.Model):
    nombreProyecto = models.CharField(max_length=78)
    estudiante = models.CharField(max_length=200)
    tema = models.CharField(max_length=100)
    profesor = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.nombreProyecto + self.estudiante + self.tema + self.profesor
    

class UsuarioSegmento(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=10,choices=TIPO_USUARIO,default="E")
    def __str__(self):
        return self.usuario.username