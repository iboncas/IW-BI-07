from django.db import models
from django.utils.timezone import now

class Pais(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100)
    descripcion = models.TextField()
    continente = models.CharField(max_length=100)
    image = models.ImageField(upload_to='travelOffersApp/static/img/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='travelOffersApp/static/img/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='ofertas')
    categorias = models.ManyToManyField(Categoria, related_name='ofertas')
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='travelOffersApp/static/img/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class FormularioContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    respondido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} - {'Respondido' if self.respondido else 'No Respondido'}"

