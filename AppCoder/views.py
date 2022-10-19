from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from AppCoder.forms import ClaseFormulario
from AppCoder.models import Ubicacion, Profesora, Clase

# Create your views here.
def mostrar_inicio(request):
    return render(request, "AppCoder/inicio.html")

def mostrar_busqueda(request):
    return render(request, "AppCoder/busqueda.html")

def buscar(request):
    if not request.GET["fecha"]:
        return HttpResponse("No enviaste datos")
    else:
        fecha_a_buscar = request.GET["fecha"]
        clases = Clase.objects.filter(fecha=fecha_a_buscar)

        contexto = {
            "fecha": fecha_a_buscar,
            "clases": clases,
        }

        return render(request, "AppCoder/resultado_busqueda.html", contexto)

def mostrar_contacto(request):
    return render(request, "AppCoder/contacto.html")

def mostrar_sobrenosotros(request):
    return render(request, "AppCoder/sobrenosotros.html")

def mostrar_formulario(request):
    if request.method != "POST":
        return render(request, "AppCoder/formulario.html")

    clase = Clase(fecha=request.POST["fecha"], nombre=request.POST["nombre"] )
    clase.save()
    return render(request, "AppCoder/inicio.html")

def mostrar_agregarprofesora(request):
    if request.method != "POST":
        return render(request, "AppCoder/agregarprofesora.html")

    profesora = Profesora(nombre=request.POST["nombre_profesora"], apellido=request.POST["apellido_profesora"], email=request.POST["email_profesora"] )
    profesora.save()
    return render(request, "AppCoder/inicio.html")

def mostrar_agregarubicacion(request):
    if request.method != "POST":
        return render(request, "AppCoder/agregarubicacion.html")

    ubicacion = Ubicacion(nombre=request.POST["nombre_ubicacion"], direccion=request.POST["direccion_ubicacion"])
    ubicacion.save()
    return render(request, "AppCoder/inicio.html")

def mostrar_formulario_2(request):
    if request.method != "POST":
        mi_formulario = ClaseFormulario
    else:
        mi_formulario = ClaseFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            clase = Clase(nombre=informacion["clase"], fecha=informacion["fecha"])
            clase.save()
            return render(request, "AppCoder/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppCoder/formulario2.html", contexto)
