from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home,crear_clientes,crear_form,busqueda,templante
app_name='cliente'
urlpatterns = [
    path("" ,home, name="home" ),
    path("clientes_creados/",crear_clientes,name="crear_clientes"),
    path("crear/", crear_form,name="crear"),
    path("busqueda/",busqueda,name="busqueda"),
    path("templates/",templante,name="template")
]
urlpatterns += staticfiles_urlpatterns()
