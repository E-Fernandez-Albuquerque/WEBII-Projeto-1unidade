from django.views.generic import TemplateView, FormView

class HomePageView(TemplateView):
    template_name = 'home.html'


class AdicionarView(FormView):
    template_name = 'adicionar.html'
    