from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    rg = models.CharField(max_length=16, unique=True)
    cpf = models.CharField(unique=True, max_length=14)

    def __str__(self):
        return self.cpf

    def get_absolute_url(self):
        return reverse('cliente:detail', kwargs={'slug': self.slug})