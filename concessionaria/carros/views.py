from django.views.generic import DetailView, ListView
from .models import Carro
from .forms import CarForm
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class CarroListView(ListView):
    model = Carro

class CarroDetailView(DetailView):
    model = Carro

@login_required
def novoVeiculo(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('/')
    else:
        form = CarForm()
        return render(request, 'adicionar.html', {'form': form})