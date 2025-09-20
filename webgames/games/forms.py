from django import forms
from django.core.exceptions import ValidationError
from .bets import splits, streets, corners, lines


class RouletteBetForm(forms.Form):

    # single = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    combo = forms.CharField(widget=forms.HiddenInput, required=False)
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

    def clean_combo(self):
        combo = self.cleaned_data['combo']
        if not combo:
            return combo

        combo_list = [int(i) for i in combo.split('-')]

        if len(combo_list) == 1:
            if int(combo_list[0]) in range(37):
                return combo

        elif len(combo_list) == 2:
            if tuple(sorted(combo_list)) in splits:
                return combo

        elif len(combo_list) == 3:
            if tuple(sorted(combo_list)) in streets:
                return combo

        elif len(combo_list) == 4:
            if tuple(sorted(combo_list)) in corners:
                return combo

        elif len(combo_list) == 6:
            if tuple(sorted(combo_list)) in lines:
                return combo

        self.add_error(None, 'You must choise correct combo. You can read about betting options & payouts in About page')


    def clean_bet_amount(self):
        bet = self.cleaned_data['bet_amount']
        if self.request.user.profile.balance < bet:
            self.add_error(None, "You don't have enough coins for such bet")
        return bet


