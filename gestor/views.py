from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Campaña, Anuncio
from .forms import CampañaForm, AnuncioForm

# ---------- CRUD CAMPAÑA ----------
class CampañaListView(ListView):
    model = Campaña
    template_name = 'gestor/campana_list.html'
    context_object_name = 'campanas'

class CampañaCreateView(CreateView):
    model = Campaña
    form_class = CampañaForm
    template_name = 'gestor/campana_form.html'
    success_url = reverse_lazy('campana_list')

class CampañaUpdateView(UpdateView):
    model = Campaña
    form_class = CampañaForm
    template_name = 'gestor/campana_form.html'
    success_url = reverse_lazy('campana_list')

class CampañaDeleteView(DeleteView):
    model = Campaña
    template_name = 'gestor/campana_confirm_delete.html'
    success_url = reverse_lazy('campana_list')

# ---------- CRUD ANUNCIO (anidado en campaña) ----------
class AnuncioListView(ListView):
    model = Anuncio
    template_name = 'gestor/anuncio_list.html'
    context_object_name = 'anuncios'

    def get_queryset(self):
        self.campana = get_object_or_404(Campaña, pk=self.kwargs['campana_id'])
        return Anuncio.objects.filter(campana=self.campana)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campana'] = self.campana
        return context

class AnuncioCreateView(CreateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'gestor/anuncio_form.html'

    def get_initial(self):
        initial = super().get_initial()
        campana = get_object_or_404(Campaña, pk=self.kwargs['campana_id'])
        initial['campana'] = campana
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campana'] = get_object_or_404(Campaña, pk=self.kwargs['campana_id'])
        return context

    def get_success_url(self):
        return reverse_lazy('anuncio_list', kwargs={'campana_id': self.kwargs['campana_id']})

class AnuncioUpdateView(UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'gestor/anuncio_form.html'

    def get_success_url(self):
        # Redirige a la lista de anuncios de la campaña del anuncio que se editó
        anuncio = self.object
        return reverse_lazy('anuncio_list', kwargs={'campana_id': anuncio.campana_id})

class AnuncioDeleteView(DeleteView):
    model = Anuncio
    template_name = 'gestor/anuncio_confirm_delete.html'

    def get_success_url(self):
        anuncio = self.object
        return reverse_lazy('anuncio_list', kwargs={'campana_id': anuncio.campana_id})