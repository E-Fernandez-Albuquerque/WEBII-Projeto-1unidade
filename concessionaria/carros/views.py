from django.views.generic import DetailView, ListView
from .models import Carro

class CarroListView(ListView):
    model = Carro

class CarroDetailView(DetailView):
    model = Carro