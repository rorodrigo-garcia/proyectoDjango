from django.http import HttpResponse
#from django.template import Context, Template 
from datetime import datetime
from django.shortcuts import render

def saludo(resquest):
    return HttpResponse ("Hola Django- Coder")  #httpResponse es una clase que va a devolver un string

def segundoSaludo(resquest):
    return HttpResponse("<h1> Esto es otra funcion</h1>")

def nombre(request,nombre : str,apellido : str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    print(f"{apellido} ,{nombre} ")
    edad = input("Edad:")
    return HttpResponse(f"{apellido} , {nombre} : edad {edad}")

def template(request):
   # mi_html = open("./templates/template.html")
   # mi_template = Template(mi_html.read())
   # mi_html.close()
    nombre = "Rodrigo"
    apellido = "Garcia"
    ahora = datetime.now().strftime("%d/%m/%Y  %H:%M:S.%f")
    datos={"nombre": nombre , "apellido" : apellido , "fecha":ahora}
   # mi_contexto = Context(datos)
   # mi_documento = mi_template.render(mi_contexto)
   # return HttpResponse (mi_documento)
    return render(request,"template.html" , datos)

def fecha_hora(request):
    
    ahora = datetime.now().strftime("%d/%m/%Y  %H:%M:S.%f")
    return HttpResponse(f"<h1> Fecha y hora : {ahora} <h1>")


def mis_notas(request):
    lista_de_notas = [2,3,4,5,6,7,8,9]
    context = {"notas" : lista_de_notas}
    return render(request,"template2.html" , context)

def template(request):
    nombre= "Rodrigo"
    apellido="Garcia"
    numeros = [1,2,3,4,5,6,7,8,9]
    datos = {"nombre":nombre, "apellido":apellido,"numeros": numeros}
    return render(request,"template3.html",datos)
    