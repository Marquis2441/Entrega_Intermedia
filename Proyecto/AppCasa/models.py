from django.db import models

# Create your models here.

class Casa(models.Model):
    nombre = models.CharField(max_length=128)
    fantasma = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nombre}'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    casa=models.ForeignKey('Casa', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    materia=models.CharField(max_length=128)
    casa=models.ForeignKey('Casa', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.nombre}, {self.apellido} Prof. de {self.materia}'