

from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('roulette/', views.Roulette.as_view(), name='roulette')

]