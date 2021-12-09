from django.db.models.expressions import Col
from django.views.generic import DetailView, ListView
from .models import Colaborador
from .forms import ColabForm
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class ColabListView(ListView):
    model = Colaborador

class ColabDetailView(DetailView):
    model = Colaborador

@login_required
def novoColab(request):
    if request.method == 'POST':
        form = ColabForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('/')
    else:
        form = ColabForm()
        return render(request, 'adicionarcolab.html', {'form': form})

@login_required
def editarColab(request, id):
    edit = get_object_or_404(Colaborador, pk=id)
    form = ColabForm(instance=edit)

    if(request.method == 'POST'):
        form = ColabForm(request.POST, instance=edit)

        if form.is_valid():
            edit.save()
            return redirect('/')
        else:
            return render(request, 'atualizarcolab.html',{'form': form, 'edit':edit})

    else:
        return render(request, 'atualizarcolab.html',{'form': form, 'edit':edit})

@login_required
def deletarColab(request, id):
    colab = get_object_or_404(Colaborador, pk=id)
    colab.delete()

    messages.info(request, 'Colaborador deletado com sucesso.')

    return redirect('/colaboradores')