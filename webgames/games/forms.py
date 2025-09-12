from django import forms

class RouletteBetForm(forms.Form):
    single = forms.CharField(widget=forms.HiddenInput())
    bet_amount = forms.IntegerField(label="Bet amount")
