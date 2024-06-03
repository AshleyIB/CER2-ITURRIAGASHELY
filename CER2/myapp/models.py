from django.db import models

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
    

class Usuario(models.Model):
    nombre= models.CharField(max_length=50)
    contrasena= models.CharField(max_length=10)
    tipo_usuario = models.CharField(max_length=10,choices=TIPO_USUARIO,default="E")
    def __str__(self):
        return self.nombre