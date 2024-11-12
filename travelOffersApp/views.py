from django.shortcuts import render

# Landing
def landing(request):
    return render(request, 'index.html')

# Todas las ofertas
def ofertas(request):
    return render(request, 'ofertas.html')

# Info de oferta
def oferta(request, offer_id):
    return render(request, 'oferta.html', {'offer_id': offer_id})

# Todos los países
def paises(request):
    return render(request, 'paises.html')

# Info de país
def pais(request, country_id):
    return render(request, 'pais.html', {'country_id': country_id})

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