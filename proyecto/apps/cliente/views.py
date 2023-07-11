from django.shortcuts import render,redirect
from .models import Pais,Cliente
from .forms import ClienteForm
from django.http import HttpRequest,HttpResponse
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
    
    return render(request,"usuario/crear.html",{"form":form})

