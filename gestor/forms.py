from django import forms
from .models import Campaña, Anuncio

class CampañaForm(forms.ModelForm):
    class Meta:
        model = Campaña
        fields = ['nombre', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo', 'imagen', 'campana']   
        widgets = {
            'campana': forms.HiddenInput(), 
        }