from typing import Dict

from django.shortcuts import render
from django.http import HttpResponse
from AppCasa.models import Casas, Estudiantes,Profesores
from AppCasa.forms import CasasFormulario, EstudiantesFormulario, ProfesoresFormulario

def inicio(request):

    return render(request, "AppCasa/inicio.html")

def estudiantes(request):

    return render(request, "AppCasa/estudiantes.html")

def casas(request):
    casas = Casas.objects.all()
    return render(request, "AppCasa/casas.html",{'casas': casas})

def profesores(request):

    return render(request, "AppCasa/profesores.html")

def casas_formulario(request):
    if request.method == 'POST':
            formulario= CasasFormulario(request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data
                casa = Casas(nombre=data['nombre'], fantasma=data['fantasma'])
                casa.save()
                return render(request, "AppCasa/inicio.html", {"exitoso": True})
    else:  # GET
            formulario= CasasFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCasa/form_casas.html", {"formulario": formulario})
# Create your views here.
