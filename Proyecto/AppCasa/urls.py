from django.urls import path

from AppCasa import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('casas/', views.casas, name="casas"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('profesores/', views.profesores, name="profesores"),
    path('crear-casa/', views.casas_formulario, name="casas_formulario"),
    path('agregar-estudiantes/', views.estudiantes_formulario, name="estudiantes_formulario"),
]