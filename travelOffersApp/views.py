from django.shortcuts import render, get_object_or_404
from .models import Pais, Categoria, Oferta

# Landing
def landing(request):
    return render(request, 'index.html')

# Todas las ofertas
def ofertas(request):
    ofertas = Oferta.objects.all()
    return render(request, 'ofertas.html', {'ofertas': ofertas})

# Info de oferta
def oferta(request, id_oferta):
    oferta = get_object_or_404(Oferta, id_oferta=id_oferta)
    return render(request, 'oferta.html', {'oferta': oferta})

# Todos los países
def paises(request):
    paises = Pais.objects.all()
    return render(request, 'paises.html', {'paises': paises})

# Info de país
def pais(request, nombre):
    pais = get_object_or_404(Pais, nombre=nombre)
    return render(request, 'pais.html', {'pais': pais})

# Todas las categorías
def categorias(request):
    return render(request, 'categorias.html')

# Info de categoría
def categoria(request, category_id):
    return render(request, 'categoria.html', {'category_id': category_id})

# Sobre Nosotros
def aboutus(request):
    return render(request, 'aboutus.html')

# Contacto
def contacto(request):
    return render(request, 'contacto.html')