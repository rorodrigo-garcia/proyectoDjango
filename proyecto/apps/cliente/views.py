from django.shortcuts import render,redirect
from .models import Pais,Cliente
from .forms import ClienteForm
from django.http import HttpRequest,HttpResponse
from datetime import date
# Create your views here.

def home(request):
    clientesRegistrados = Cliente.objects.all()
    contexto = {"clientes" : clientesRegistrados}
    #return render (request,"index.html" , {"clientes" : clientesRegistrados})
    return render(request,"cliente/index.html" , contexto)

def crear_clientes(request):
    from datetime import date
    p1 = Pais(nombre = "Arg")
    p2 = Pais(nombre="Ch")
    p3 = Pais(nombre = "Mx")
    p1.save()
    p2.save()
    cliente1 = Cliente(nombre="rodrigo" , apellido = "Garcia " , nacimiento = date(1997,1,1) ,pais_origen_id=p1)
    cliente2 = Cliente(nombre = "Mati" , apellido= "Erusalimsky",nacimiento = date(1996,7,10) , pais_origen_id=p2 )


    cliente1.save()
    cliente2.save()
    return redirect("cliente:home")


def crear_form(request: HttpRequest) -> HttpResponse:
    
    if request.method == "POST":
        form =ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = ClienteForm()
    return render(request,"cliente/crear.html",{"form":form})

def busqueda(request):
    cliente_nombre = Cliente.objects.filter(nombre__contains="o")
    cliente_nacimiento = Cliente.objects.filter(nacimiento__gt = date(2000,1,1))
    contexto = {
        "cliente_nombre": cliente_nombre,
        "cliente_nacimiento" : cliente_nacimiento
    }
    return render(request,"cliente/busqueda.html", contexto)

def templante(request):
    return  render(request,'cliente/template2.html')