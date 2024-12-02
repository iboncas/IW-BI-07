from django.shortcuts import render, get_object_or_404
from .models import Pais, Categoria, Oferta
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

# Landing
class LandingView(TemplateView):
    template_name = 'index.html'  # Especifica el template que se renderiza

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paises = Pais.objects.all()
        baratas = []
        for pais in paises:
            barata = Oferta.objects.filter(pais=pais, disponible=True).order_by('precio').first()
            if barata:
                baratas.append(barata)
        context['ofertas_mas_baratas'] = baratas
        return context

# Todas las ofertas
class OfertasView(ListView):
    model = Oferta
    template_name = 'ofertas.html'
    context_object_name = 'ofertas'

# Info de oferta
class OfertaView(DetailView):
    model = Oferta
    template_name = 'oferta.html'
    context_object_name = 'oferta'

# Todos los países
class PaisesView(ListView):
    model = Pais
    template_name = 'paises.html'
    context_object_name = 'paises'

# Info de país
class PaisView(DetailView):
    model = Pais
    template_name = 'pais.html'
    context_object_name = 'pais'

# Todas las categorías
class CategoriasView(ListView):
    model = Categoria
    template_name = 'categorias.html'
    context_object_name = 'categorias'

# Info de categoría
class CategoriaView(DetailView):
    model = Categoria
    template_name = 'categoria.html'
    context_object_name = 'categoria'

# Sobre Nosotros
class AboutUsView(TemplateView):
    template_name = "aboutus.html"

# Contacto
def contacto(request):
    return render(request, 'contacto.html')