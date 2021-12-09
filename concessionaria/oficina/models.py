from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse

# Create your models here.

class Atendimento(models.Model):
    cliente = models.CharField(max_length=255)
    colaborador = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    data = models.DateField()
    reparo = models.TextField(default='manutenção básica')

    def __str__(self):
        return self.cliente

    def get_absolute_url(self):
        return reverse('atendimento:detail', kwargs={'slug': self.slug})