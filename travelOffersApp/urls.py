from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('ofertas/<int:offer_id>/', views.oferta, name='oferta'),
    path('paises/', views.paises, name='paises'),
    path('paises/<int:country_id>/', views.pais, name='pais'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<int:category_id>/', views.categoria, name='categoria'),
]

