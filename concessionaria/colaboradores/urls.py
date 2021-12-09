from django.urls import path

from . import views

app_name = 'colab'

urlpatterns = [
    path('', views.ColabListView.as_view(), name='list'),
    path("<slug:slug>/", views.ColabDetailView.as_view(), name='detail'),
    path('manage/adicionar-colaborador/', views.novoColab, name='adicionar'),
    path('manage/atualizar-colaborador/<int:id>', views.editarColab, name='atualizar'),
    path('manage/deletar-colaborador/<int:id>', views.deletarColab, name='deletar'),
]