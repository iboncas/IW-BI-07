from django.contrib import admin
from .models import Pais, Categoria, Oferta, FormularioContacto

def marcar_como_disponible(modeladmin, request, queryset):
    queryset.update(disponible=True)

marcar_como_disponible.short_description = "Marcar como disponible"

# Cambiar el título de la página de administración
admin.site.site_header = "Panel de Administración - Travel Offers"
admin.site.site_title = "Travel Offers Admin"
admin.site.index_title = "Bienvenido al Panel de Administración"

class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'continente')  # Mostrar estas columnas
    search_fields = ('nombre',)  # Campo de búsqueda
    list_filter = ('continente',)  # Agregar filtro por continente
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # Mostrar el nombre y la descripción
    search_fields = ('nombre', 'descripcion')  # Búsqueda por nombre y descripción

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'pais', 'disponible')  # Mostrar columnas clave
    list_editable = ('precio', 'disponible')  # Hacer editables estas columnas
    search_fields = ('nombre', 'pais__nombre')  # Buscar por título y país
    list_filter = ('disponible', 'pais')  # Agregar filtros
    actions = [marcar_como_disponible]
    
class FormularioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'titulo', 'respondido') # Mostrar las columnas indicadas
    search_fields = ('nombre', 'email') # Buscar por esos campos
    list_filter = ('respondido',) # Filtro por respondido

admin.site.register(Pais, PaisAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(FormularioContacto, FormularioAdmin)

