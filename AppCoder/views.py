from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from AppCoder.models import Familia

# Create your views here.
def crear_familiar(request):
    template = loader.get_template("template.html")

    familiar1 = Familia(nombre = "Amparo", apellido = "Caceres", email = "amparocaceres@gmail.com")
    familiar2 = Familia(nombre = "Silvia", apellido = "Roldan", email = "silviar@gmail.com")
    familiar3 = Familia(nombre = "Mario", apellido = "Pardini", email = "mariop@gmail.com")
    dict_context = {
        "familiar1": familiar1.nombre,
        "familiar2": familiar2.nombre,
        "familiar3": familiar3.nombre,
    }
    
    res = template.render(dict_context)
    return HttpResponse(res)

def mostrar_inicio(request):
    return render(request, "AppCoder/inicio.html")

def mostrar_contacto(request):
    return render(request, "AppCoder/contacto.html")