from django.views.generic import DetailView, ListView
from .models import Carro
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class CarroListView(ListView):
    model = Carro

class CarroDetailView(LoginRequiredMixin, DetailView):
    model = Carro