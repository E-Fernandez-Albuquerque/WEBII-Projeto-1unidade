from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse

# Create your models here.

class Carro(models.Model):
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    placa = models.CharField(max_length=8, unique=True)
    potencia = models.IntegerField()
    cilindrada = models.CharField(max_length=4)
    cor = models.CharField(max_length=30)
    passageiros = models.IntegerField()
    publicacao = models.DateTimeField(auto_now_add=True)
    fabricacao = models.IntegerField()

    def __str__(self):
        return self.placa

    def get_absolute_url(self):
        return reverse('carros:detail', kwargs={'slug': self.slug})