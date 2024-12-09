# forms.py
from django import forms
from .models import FormularioContacto

class FormularioContactoForm(forms.ModelForm):
    class Meta:
        model = FormularioContacto
        fields = ['nombre', 'email', 'titulo', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'}),
        }