import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, ListView
from .forms import RouletteBetForm
from .bets import is_win, fields, fields_in_order
from .models import RouletteSpin, User
from .bets import bet_dict, combo_variants, bets_variants


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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.past_balance = None

    def form_valid(self, form):
        bet = form.cleaned_data['bet_amount']
        bet_type = form.cleaned_data['bet_type']
        print(bet_type)
        if bet_type <= 5:
            bet_value = form.cleaned_data[bet_dict[bet_type]]
        else:
            form_value = form.cleaned_data[bet_dict[bet_type]]

            bet_value = combo_variants[int(bet_type)][tuple(sorted(int(i) for i in form_value.split('-')))]

        user = self.request.user
        if user.is_authenticated:
            user.profile.balance -= bet
            self.request.session['past_balance'] =  user.profile.balance
            user.profile.save()
        else:
            user = None

        spin = RouletteSpin.objects.create(
            user=user,
            bet_amount=bet,
            bet_type=bet_type,
            bet_value=bet_value,

        )
        self.spin = spin
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('spin', kwargs={'spin_id': self.spin.id,})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


def roulette_spin(request, spin_id):
    spin = get_object_or_404(RouletteSpin, id=spin_id, user=request.user)

    if not spin.result_value:
        spin.result_value = random.randint(1, 360)

        if is_win(spin):
            spin.is_win = True

        spin.save()
        spin.user.profile.save()

        bet_value = spin.bet_value

        if spin.bet_type >=6:
            bet_value  = list([k for k, v in combo_variants[spin.bet_type].items() if v == spin.bet_value][0])
    else:
        return redirect('roulette')

    return render(request, 'games/roulette_spin_form.html',
                  {
        'fields': fields,
        'fields_in_order': fields_in_order,
        'bet_amount': spin.bet_amount,
        'bet_type': spin.bet_type,
        'bet_value': bet_value,
        'is_win': spin.is_win,
        'result_value': spin.result_value,
        'win_value': spin.win_value,
        'past_balance': request.session['past_balance'],
    })

class GamesHistory(LoginRequiredMixin, ListView):
    model = RouletteSpin
    template_name = 'games/games_history.html'
    context_object_name = 'games'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for game in context['games']:
            if game.bet_type in combo_variants:
                collection = combo_variants[game.bet_type]
                game.bet_value_display = [k for k in collection if collection[k] == game.bet_value][0]
            else:

                game.bet_value_display = bets_variants[game.bet_type][game.bet_value]

        return context

    def get_queryset(self):
        games_list = RouletteSpin.objects.filter(user=self.request.user)
        return games_list



def contacts(request):
    return render(request, 'games/contacts.html')

def about(request):
    return render(request, 'games/about.html')


