from django.urls import path

from . import views

app_name = 'carros'

urlpatterns = [
    path('', views.CarroListView.as_view(), name='list'),
    path("<slug:slug>/", views.CarroDetailView.as_view(), name='detail'),
    path('manage/adicionar-registro/', views.novoVeiculo, name='adicionar'),
    path('manage/atualizar-registro/<int:id>', views.editarVeiculo, name='atualizar'),
    path('manage/deletar-registro/<int:id>', views.deletarVeiculo, name='deletar'),
]