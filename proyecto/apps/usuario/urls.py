from django.urls import path
from .views import funcion
urlpatterns = [    
    path('usuario', funcion  ,name="funcion")
]
