from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('adicionar-registro/', views.AdicionarView.as_view(), name='adicionar')
]