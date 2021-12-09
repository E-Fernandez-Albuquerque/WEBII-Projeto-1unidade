from django.urls import path

from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='list'),
    path("<slug:slug>/", views.ClienteDetailView.as_view(), name='detail'),
    path('manage/adicionar-cliente/', views.novoCliente, name='adicionar'),
    path('manage/atualizar-cliente/<int:id>', views.editarCliente, name='atualizar'),
    path('manage/deletar-cliente/<int:id>', views.deletarCliente, name='deletar'),
]