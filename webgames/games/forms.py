from django import forms
from django.core.exceptions import ValidationError


class RouletteBetForm(forms.Form):

    single = forms.IntegerField(widget=forms.HiddenInput())
    bet_amount = forms.IntegerField(label="Bet amount", min_value=10)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean_bet_amount(self):
        bet = self.cleaned_data['bet_amount']
        if self.request.user.profile.balance < bet:
            raise ValidationError("You don't have enough coins for such bet")
        return bet

class RouletteSpinForm(forms.Form):
    spin_result = forms.FloatField(widget=forms.HiddenInput())

