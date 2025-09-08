from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomePage(TemplateView):
    template_name = 'games/index.html'
    extra_context = {
        'title': 'Home',
    }

class Roulette(TemplateView):
    template_name = 'games/roulette.html'
    extra_context = {
        'title': 'Roulette',
    }
