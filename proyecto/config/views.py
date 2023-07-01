from django.http import HttpResponse
from django.template import Context, Template 

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
    mi_html = open("./templates/template.html")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse (mi_documento)