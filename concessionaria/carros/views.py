from django.views.generic import DetailView, ListView
from .models import Carro
from .forms import CarForm
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@login_required
def editarVeiculo(request, id):
    edit = get_object_or_404(Carro, pk=id)
    form = CarForm(instance=edit)

    if(request.method == 'POST'):
        form = CarForm(request.POST, instance=edit)

        if form.is_valid():
            edit.save()
            return redirect('/')
        else:
            return render(request, 'atualizar.html',{'form': form, 'edit':edit})

    else:
        return render(request, 'atualizar.html',{'form': form, 'edit':edit})

@login_required
def deletarVeiculo(request, id):
    carro = get_object_or_404(Carro, pk=id)
    carro.delete()

    messages.info(request, 'Carro deletado com sucesso.')

    return redirect('/concessionaria')
