from django.contrib import admin
from django.urls import path
from AppCoder.views import mostrar_agregarprofesora, mostrar_formulario, mostrar_inicio, mostrar_contacto, mostrar_sobrenosotros, mostrar_agregarubicacion, mostrar_formulario_2, mostrar_busqueda, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', mostrar_inicio, name="inicio"),
    path('contacto/', mostrar_contacto, name="contacto"),
    path('sobrenosotros/', mostrar_sobrenosotros, name="sobrenosotros"),
    path('formulario/', mostrar_formulario, name="formulario"),
    path('agregarprofesora/', mostrar_agregarprofesora, name="agregarprofesora"),
    path('agregarubicacion/', mostrar_agregarubicacion, name="agregarubicacion"),
    path('formulario2/', mostrar_formulario_2, name="formulario2"),
    path('busqueda/', mostrar_busqueda, name="busqueda"),
    path('buscar/', buscar),
    
]