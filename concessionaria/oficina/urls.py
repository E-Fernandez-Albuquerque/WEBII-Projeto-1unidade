from django.urls import path

from . import views

app_name = 'oficina'

urlpatterns = [
    path('', views.AtendimentoListView.as_view(), name='list'),
    path("<slug:slug>/", views.AtendimentoDetailView.as_view(), name='detail'),
    path('manage/adicionar-atendimento/', views.novoAtendimento, name='adicionar'),
    path('manage/atualizar-atendimento/<int:id>', views.editarAtendimento, name='atualizar'),
    path('manage/deletar-atendimento/<int:id>', views.deletarAtendimento, name='deletar'),
]