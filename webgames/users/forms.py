from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.forms.models import ModelForm

from .models import Profile
from .utils import age_validator


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username')
    date_of_birth = forms.DateField(label='Birthday', widget=forms.DateInput(attrs={"type": "date"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2' ]
        labels = {'email': 'E-mail'}

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exists')
        return email

    def clean_date_of_birth(self):
        date = self.cleaned_data['date_of_birth']
        if age_validator(date):
            return date
        raise forms.ValidationError("Invalid age")

    def save(self, commit=True):
        user = super().save(commit=commit)
        Profile.objects.create(
            user=user,
            date_of_birth=self.cleaned_data["date_of_birth"],
            balance = 500 + self.request.session['balance'],
        )
        return user

class ProfileUserForm(ModelForm):
    username = forms.CharField(label='username', disabled=True)
    email = forms.CharField(label='E-mail', disabled=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'Name',
            'last_name': 'Surname',
        }

        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),

        }

class PasswordChangeUserForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='New password',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Password confirm',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))