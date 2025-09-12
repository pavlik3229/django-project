from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import RouletteBetForm
from .utils import fields, fields_in_order
# Create your views here.


class HomePage(TemplateView):
    template_name = 'games/home.html'

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
        'title': 'roulette',
        'fields': fields,
        'fields_in_order': fields_in_order,
    }

    def form_valid(self, form):
        bet = form.cleaned_data['bet_amiunt']
        number = form.cleaned_data['single']
        print(bet)
        print(number)


def contacts(request):
    return render(request, 'games/contacts.html')

def about(request):
    return render(request, 'games/about.html')


