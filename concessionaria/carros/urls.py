from django.urls import path

from . import views

app_name = 'carros'

urlpatterns = [
    path('', views.CarroListView.as_view(), name='list'),
    path("<slug:slug>/", views.CarroDetailView.as_view(), name='detail'),
]