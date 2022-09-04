from typing import Dict

from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):

    return render(request, "AppCasa/inicio.html")

def estudiantes(request):

    return render(request, "AppCasa/estudiantes.html")

def casas(request):

    return render(request, "AppCasa/casas.html")

def profesores(request):

    return render(request, "AppCasa/profesores.html")


# Create your views here.
