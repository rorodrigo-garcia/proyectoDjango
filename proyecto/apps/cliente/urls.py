from django.urls import path
from .views import home,crear_clientes,crear_form
app_name='cliente'
urlpatterns = [
    path("" ,home, name="home" ),
    path("clientes_creados/",crear_clientes,name="crear_clientes"),
    path("crear/", crear_form,name="crear")
]
