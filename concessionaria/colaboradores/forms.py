from django import forms
from django.db.models import fields

from .models import Colaborador

class ColabForm(forms.ModelForm):

    class Meta:
        model = Colaborador
        fields = ('nome', 'sobrenome', 'rg', 'cpf', 'cargo', 'slug')