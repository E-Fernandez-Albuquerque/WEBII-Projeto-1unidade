from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse

# Create your models here.

class Colaborador(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    rg = models.CharField(max_length=16, unique=True)
    cpf = models.CharField(unique=True, max_length=14)
    cargo = models.CharField(max_length=255)


    def __str__(self):
        return self.cpf

    def get_absolute_url(self):
        return reverse('colaborador:detail', kwargs={'slug': self.slug})