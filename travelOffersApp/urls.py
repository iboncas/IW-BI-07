from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingView.as_view(), name='landing'),
    path('ofertas/', views.OfertasView.as_view(), name='ofertas'),
    path('ofertas/<int:pk>/', views.OfertaView.as_view(), name='oferta'),
    path('paises/', views.PaisesView.as_view(), name='paises'),
    path('paises/<str:pk>/', views.PaisView.as_view(), name='pais'),
    path('categorias/', views.CategoriasView.as_view(), name='categorias'),
    path('categorias/<str:pk>/', views.CategoriaView.as_view(), name='categoria'),
    path('aboutus/', views.AboutUsView.as_view(), name='aboutus'),
    path('contacto/', views.contacto, name='contacto'),
]
