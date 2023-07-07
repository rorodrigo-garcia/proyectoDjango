from django.shortcuts import render
from .models import Pais
# Create your views here.

def home(request):
    clientesRegistrados = Pais.objects.all()
    contexto = {"clientes" : clientesRegistrados}
    #return render (request,"index.html" , {"clientes" : clientesRegistrados})
    return render(request,"cliente/index.html" , contexto)