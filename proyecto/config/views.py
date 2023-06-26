from django.http import HttpResponse

def saludo(resquest):
    return HttpResponse ("Hola Django- Coder")  #httpResponse es una clase que va a devolver un string

def segundoSaludo(resquest):
    return HttpResponse("<h1> Esto es otra funcion</h1>")