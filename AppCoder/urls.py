from django.contrib import admin
from django.urls import path
from AppCoder.views import crear_familiar, mostrar_inicio, mostrar_contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear-familiar/', crear_familiar),
    path('inicio/', mostrar_inicio, name="inicio"),
    path('contacto/', mostrar_contacto, name="contacto")
]