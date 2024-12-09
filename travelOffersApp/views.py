from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Pais, Categoria, Oferta
from .forms import FormularioContactoForm
from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView, ListView, DetailView

# Landing
class LandingView(TemplateView):
    template_name = 'index.html'  # Especifica el template que se renderiza

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paises = get_list_or_404(Pais)
        baratas = []
        for pais in paises:
            barata = Oferta.objects.filter(pais=pais, disponible=True).order_by('precio').first()
            if barata:
                baratas.append(barata)
        # Traducción del título para las ofertas más baratas
        context['titulo_ofertas'] = _("Ofertas más baratas")
        context['ofertas_mas_baratas'] = baratas
        return context

# Todas las ofertas
class OfertasView(ListView):
    model = Oferta
    template_name = 'ofertas.html'
    context_object_name = 'ofertas'
    
    def get_queryset(self):
        return get_list_or_404(Oferta)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traducción del título para la lista de ofertas
        context['titulo_ofertas'] = _("Todas las ofertas")
        return context

# Info de oferta
class OfertaView(DetailView):
    model = Oferta
    template_name = 'oferta.html'
    context_object_name = 'oferta'
    
    def get_object(self, queryset = None):
        return get_object_or_404(Oferta, id_oferta=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traducción del título de la página de detalle de oferta
        context['titulo_oferta'] = _("Detalles de la oferta")
        return context

# Todos los países
class PaisesView(ListView):
    model = Pais
    template_name = 'paises.html'
    context_object_name = 'paises'
    
    def get_queryset(self):
        return get_list_or_404(Pais)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traducción del título para la lista de países
        context['titulo_paises'] = _("Todos los países")
        return context

# Info de país
class PaisView(DetailView):
    model = Pais
    template_name = 'pais.html'
    context_object_name = 'pais'
    
    def get_object(self, queryset=None):
        return get_object_or_404(Pais, nombre=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traducción del título para los detalles de país
        context['titulo_pais'] = _("Detalles del país")
        return context

# Todas las categorías
class CategoriasView(ListView):
    model = Categoria
    template_name = 'categorias.html'
    context_object_name = 'categorias'
    
    def get_queryset(self):
        return get_list_or_404(Categoria)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traducción del título para la lista de categorías
        context['titulo_categorias'] = _("Todas las categorías")
        return context

# Info de categoría
class CategoriaView(DetailView):
    model = Categoria
    template_name = 'categoria.html'
    context_object_name = 'categoria'
    
    def get_object(self, queryset=None):
        return get_object_or_404(Categoria, nombre=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traducción del título para los detalles de categoría
        context['titulo_categoria'] = _("Detalles de la categoría")
        return context

# Sobre Nosotros
class AboutUsView(TemplateView):
    template_name = "aboutus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traducción del título para la página Sobre Nosotros
        context['titulo_sobre_nosotros'] = _("Sobre Nosotros")
        return context

# Contacto
def contacto(request):
    success = False
    if request.method == 'POST':
        form = FormularioContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el mensaje en la base de datos
            success = True
    else:
        form = FormularioContactoForm()

    return render(request, 'contacto.html', {
        'titulo_contacto': _("Contáctanos"),
        'form': form,
        'success': success
    })