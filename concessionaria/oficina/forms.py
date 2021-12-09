from django import forms
from django.db.models import fields

from .models import Atendimento

class AtendimentoForm(forms.ModelForm):

    class Meta:
        model = Atendimento
        fields = ('cliente', 'colaborador', 'data', 'reparo', 'slug')