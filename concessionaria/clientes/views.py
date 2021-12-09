from django.db.models.expressions import Col
from django.views.generic import DetailView, ListView
from .models import Cliente
from .forms import ClienteForm
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class ClienteListView(ListView):
    model = Cliente

class ClienteDetailView(DetailView):
    model = Cliente

@login_required
def novoCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('/')
    else:
        form = ClienteForm()
        return render(request, 'adicionarcliente.html', {'form': form})

@login_required
def editarCliente(request, id):
    edit = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=edit)

    if(request.method == 'POST'):
        form = ClienteForm(request.POST, instance=edit)

        if form.is_valid():
            edit.save()
            return redirect('/')
        else:
            return render(request, 'atualizarcliente.html',{'form': form, 'edit':edit})

    else:
        return render(request, 'atualizarcliente.html',{'form': form, 'edit':edit})

@login_required
def deletarCliente(request, id):
    colab = get_object_or_404(Cliente, pk=id)
    colab.delete()

    messages.info(request, 'Cliente deletado com sucesso.')

    return redirect('/clientes')