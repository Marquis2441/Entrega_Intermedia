from typing import Dict

from django.shortcuts import render
from django.http import HttpResponse
from AppCasa.models import Casas, Estudiantes,Profesores
from AppCasa.forms import CasasFormulario, EstudiantesFormulario, ProfesoresFormulario

def inicio(request):

    return render(request, "AppCasa/inicio.html")

def estudiantes(request):
    estudiantes = Estudiantes.objects.all()  
    return render(request, "AppCasa/estudiantes.html",{'estudiantes':estudiantes})

def casas(request):
    casas = Casas.objects.all()
    return render(request, "AppCasa/casas.html",{'casas': casas})

def profesores(request):
    profesores = Profesores.objects.all()
    return render(request, "AppCasa/profesores.html",{'profesores': profesores})

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

def estudiantes_formulario(request):
    if request.method == 'POST':
            formulario= EstudiantesFormulario(request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data
                estudiante = Estudiantes(nombre=data['nombre'], apellido=data['apellido'],casa=data['casa'])
                estudiante.save()
                return render(request, "AppCasa/inicio.html", {"exitoso": True})
    else:  # GET
            formulario= EstudiantesFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCasa/form_estudiantes.html", {"formulario": formulario})

def profesores_formulario(request):
    if request.method == 'POST':
            formulario= ProfesoresFormulario(request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data
                profesor = Profesores(nombre=data['nombre'], apellido=data['apellido'],materia=data['materia'],casa=data['casa'])
                profesor.save()
                return render(request, "AppCasa/inicio.html", {"exitoso": True})
    else:  # GET
            formulario= ProfesoresFormulario()  # Formulario vacio para construir el html
    return render(request, "AppCasa/form_profesores.html", {"formulario": formulario})