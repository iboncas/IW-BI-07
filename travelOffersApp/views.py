from django.shortcuts import render, get_object_or_404
from .models import Pais, Categoria, Oferta
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Landing
def landing(request):
    paises = Pais.objects.all()
    baratas = []
    for pais in paises:
        barata = (Oferta.objects.filter(pais=pais, disponible=True).order_by('precio').first())
        if barata:
            baratas.append(barata)
    contexto = {'ofertas_mas_baratas': baratas}
    return render(request, 'index.html', contexto)

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
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

# Info de categoría
def categoria(request, nombre):
    categoria = get_object_or_404(Categoria, nombre=nombre)
    return render(request, 'categoria.html', {'categoria': categoria})

# Sobre Nosotros
def aboutus(request):
    return render(request, 'aboutus.html')

# Contacto
def contacto(request):
    return render(request, 'contacto.html')
