from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from .forms import LoginUserForm, ProfileUserForm, RegisterUserForm


# Create your views here.


class LoginUser(LoginView):
    template_name = 'users/login.html'
    form_class = LoginUserForm

class LogoutUser(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("home")

class RegisterUser(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class UserProfile(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['balance'] = self.request.user.profile.balance
        context['date_of_birth'] = self.request.user.profile.date_of_birth
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


