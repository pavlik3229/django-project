import random

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView
from .forms import RouletteBetForm, RouletteSpinForm
from .utils import fields, fields_in_order, coordinates
from .models import RouletteSpin, User


# Create your views here.

def is_win(spin: RouletteSpin):

    win_range = coordinates[spin.bet_type]
    return win_range[0] < spin.result_value < win_range[1]



class HomePage(TemplateView):
    template_name = 'games/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "balance" not in self.request.session:
            self.request.session["balance"] = 200
        context["balance"] = self.request.session["balance"]
        return context



class RouletteBet(FormView):
    form_class = RouletteBetForm
    template_name = 'games/roulette_bet_form.html'
    extra_context = {
        'title': 'roulette_bet',
        'fields': fields,
        'fields_in_order': fields_in_order,
    }
    success_url = reverse_lazy('roulette')

    def form_valid(self, form):
        bet = form.cleaned_data['bet_amount']
        number = form.cleaned_data['single']
        user = self.request.user
        if user.is_authenticated:
            user.profile.balance -= bet
            user.profile.save()
        else:
            user = None

        spin = RouletteSpin.objects.create(
            user=user,
            bet_amount=bet,
            bet_type=0,
            bet_value=number,

        )
        self.spin = spin
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('spin', kwargs={'spin_id': self.spin.id})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


def roulette_spin(request, spin_id):
    spin = get_object_or_404(RouletteSpin, id=spin_id, user=request.user)
    spin.result_value = random.randint(1, 360)
    if is_win(spin):
        spin.is_win = True

    return render(request, 'games/roulette_spin_form.html',
                  {
        'fields': fields,
        'fields_in_order': fields_in_order,
        'bet_amount': spin.bet_amount,
        'bet_type': spin.bet_type,
        'bet_value': spin.bet_value,
        'is_win': spin.is_win,
        'result_value': spin.result_value,
    })




def contacts(request):
    return render(request, 'games/contacts.html')

def about(request):
    return render(request, 'games/about.html')


