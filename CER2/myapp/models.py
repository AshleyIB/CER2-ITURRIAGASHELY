from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombreProyecto = models.CharField(max_length=78)
    estudiante = models.CharField(max_length=200)
    tema = models.CharField(max_length=100)
    profesor = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.nombreProyecto