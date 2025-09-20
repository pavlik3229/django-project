from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

class RouletteSpin(models.Model):
    class BetType(models.IntegerChoices):
        SINGLE = 0, 'Single'
        COLOR = 1, 'Color'
        EVEN_ODD= 2, 'Even/Odd'
        LOW_HIGH = 3, 'Low/High'
        DOZENS = 4, 'Dozens'
        COLUMNS = 5, 'Columns'
        SPLITS = 6, 'Splits'
        STREETS = 7, 'Streets'
        CORNERS = 8, 'Corners'
        LINES = 9, 'Six lines'

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='spins', verbose_name='user')
    bet_amount = models.IntegerField(default=10, verbose_name='Bet amount')
    bet_type = models.IntegerField(choices=BetType.choices, verbose_name='Bet type')
    bet_value = models.IntegerField(verbose_name='Bet value')
    result_value = models.FloatField(null=True, verbose_name='Result value')
    is_win = models.BooleanField(default=False, verbose_name='Is win')
    win_value = models.IntegerField(null=True, verbose_name='Win value')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Spin time')

    class Meta:
        verbose_name = 'Spin'
        verbose_name_plural = 'Spins'
        ordering = ['-time_create']


