from django import forms
from django.db.models import fields

from .models import Carro

class CarForm(forms.ModelForm):

    class Meta:
        model = Carro
        fields = ('marca', 'modelo', 'placa', 'potencia', 'cilindrada', 'cor', 'passageiros', 'fabricacao', 'slug')