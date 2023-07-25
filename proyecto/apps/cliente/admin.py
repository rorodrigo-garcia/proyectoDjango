from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Pais)
admin.site.register(models.Cliente)
#admin.site.register(models.ProductoCategoria)

@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    list_filter=("nombre",)
