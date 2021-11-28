from django.contrib import admin
from .models import Carro
# Register your models here.


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'placa', 'fabricacao', 'cor', 'slug')
    prepopulated_fields = {'slug': ('modelo', 'placa',)}