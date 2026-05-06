from django.contrib import admin
from .models import Campaña, Anuncio

@admin.register(Campaña)
class CampañaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')

@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'campana', 'imagen')