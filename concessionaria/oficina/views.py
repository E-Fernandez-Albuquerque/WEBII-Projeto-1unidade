from django.db.models.expressions import Col
from django.views.generic import DetailView, ListView
from .models import Atendimento
from .forms import AtendimentoForm
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class AtendimentoListView(ListView):
    model = Atendimento

class AtendimentoDetailView(DetailView):
    model = Atendimento

@login_required
def novoAtendimento(request):
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('/')
    else:
        form = AtendimentoForm()
        return render(request, 'adicionaratendimento.html', {'form': form})

@login_required
def editarAtendimento(request, id):
    edit = get_object_or_404(Atendimento, pk=id)
    form = AtendimentoForm(instance=edit)

    if(request.method == 'POST'):
        form = AtendimentoForm(request.POST, instance=edit)

        if form.is_valid():
            edit.save()
            return redirect('/')
        else:
            return render(request, 'atualizaratendimento.html',{'form': form, 'edit':edit})

    else:
        return render(request, 'atualizaratendimento.html',{'form': form, 'edit':edit})

@login_required
def deletarAtendimento(request, id):
    attend = get_object_or_404(Atendimento, pk=id)
    attend.delete()

    messages.info(request, 'Cliente deletado com sucesso.')

    return redirect('/oficina')