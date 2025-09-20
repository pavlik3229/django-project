
from django.urls import path
from . import views

from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('register/', views.RegisterUser.as_view(), name='register'),

    path('password_change/', views.PasswordChangeUser.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneUser.as_view(), name='password_change_done'),

    path('password-reset/', views.PasswordResetUser.as_view(), name='password_reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/', views.PasswordResetConfirmUser.as_view(), name='password_reset_confirm'),

    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]