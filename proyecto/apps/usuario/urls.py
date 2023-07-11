from django.urls import path
from .views import funcion
urlpatterns = [    
    path('', funcion  ,name="funcion")
]
