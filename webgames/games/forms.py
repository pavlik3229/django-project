from django import forms
from django.core.exceptions import ValidationError


class RouletteBetForm(forms.Form):

    single = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    color = forms.BooleanField(widget=forms.HiddenInput(), required=False)
    even_odd = forms.BooleanField(widget=forms.HiddenInput, required=False)
    low_high = forms.BooleanField(widget=forms.HiddenInput, required=False)
    dozen = forms.IntegerField(widget=forms.HiddenInput, required=False)
    column = forms.IntegerField(widget=forms.HiddenInput, required=False)

    bet_type = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    bet_amount = forms.IntegerField(label="Bet amount", min_value=10)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)


    def clean_bet_amount(self):
        bet = self.cleaned_data['bet_amount']
        if self.request.user.profile.balance < bet:
            raise ValidationError("You don't have enough coins for such bet")
        return bet


