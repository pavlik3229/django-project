from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import RouletteBetForm

# Create your views here.


class HomePage(TemplateView):
    template_name = 'games/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "balance" not in self.request.session:
            self.request.session["balance"] = 200
        context["balance"] = self.request.session["balance"]
        return context



class Roulette(FormView):
    form_class = RouletteBetForm
    template_name = 'games/roulette.html'
    extra_context = {
        'title': 'Roulette',
    }
