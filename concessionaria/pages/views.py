from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.http import HttpResponse, request

class HomePageView(TemplateView):
    template_name = 'home.html'

'''
class AdicionarView(FormView):
    template_name = 'adicionar.html'
'''

