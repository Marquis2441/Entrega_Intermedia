from socket import fromshare
from django import forms

class CasasFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    fantasma = forms.CharField(max_length=128)


class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    casa=forms.CharField(max_length=128)


class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    materia=forms.CharField(max_length=128)
    casa=forms.CharField(max_length=128)
