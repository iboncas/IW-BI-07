from django.shortcuts import render, get_object_or_404
from .models import Pais, Categoria, Oferta
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django import forms
from django.core.mail import send_mail
from django.conf import settings

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

# Definimos el formulario
class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True, label="Nombre")
    email = forms.EmailField(required=True, label="Email")
    titulo = forms.CharField(max_length=100, required=True, label="Título")
    mensaje = forms.CharField(widget=forms.Textarea, required=True, label="Mensaje")

# Contacto
class ContactoView(FormView):
    template_name = 'contacto.html'
    form_class = ContactForm
    success_url = '/contacto/'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
