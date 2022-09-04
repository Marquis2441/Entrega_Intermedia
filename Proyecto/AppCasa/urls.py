from django.urls import path

from AppCasa import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('casas/', views.casas, name="casas"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('profesores/', views.profesores, name="profesores"),

]