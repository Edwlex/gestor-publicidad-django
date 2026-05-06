from django.urls import path
from . import views

urlpatterns = [
    # Campaña
    path('', views.CampañaListView.as_view(), name='campana_list'),
    path('campanas/nueva/', views.CampañaCreateView.as_view(), name='campana_create'),
    path('campanas/<int:pk>/editar/', views.CampañaUpdateView.as_view(), name='campana_update'),
    path('campanas/<int:pk>/eliminar/', views.CampañaDeleteView.as_view(), name='campana_delete'),

    # Anuncios anidados en campaña
    path('campanas/<int:campana_id>/anuncios/', views.AnuncioListView.as_view(), name='anuncio_list'),
    path('campanas/<int:campana_id>/anuncios/nuevo/', views.AnuncioCreateView.as_view(), name='anuncio_create'),
    path('anuncios/<int:pk>/editar/', views.AnuncioUpdateView.as_view(), name='anuncio_update'),
    path('anuncios/<int:pk>/eliminar/', views.AnuncioDeleteView.as_view(), name='anuncio_delete'),
]