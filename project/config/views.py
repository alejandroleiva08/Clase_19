from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# from django.template import Context, Template


def saludo(request):
    return HttpResponse("Hola Django - Coder")


def saludo_vista(request):
    return HttpResponse("<h1>Segunda vista</h1>")


def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")


def probando_template(request):
    nombre = "Louis"
    apellido = "Van Beethoven"
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:S.%f")
    datos = {"nombre": nombre, "apellido": apellido}
    datos["fecha"] = ahora
    return render(request, "template1.html", datos)


def fecha_hora(request):
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:S.%f")
    return HttpResponse(f"<h1> ⌛ Fecha y hora: {ahora} </h1>")


def mis_notas(request):
    lista_de_notas = [2, 3, 5, 7, 9, 10, 10]
    contexto = {"notas": lista_de_notas}
    return render(request, "notas.html", contexto)


def diccionario(request):
    mi_diccionario = {"persona": {"nombre": "Cintia", "edad": 38}}

    return render(request, "prueba.html", mi_diccionario)
