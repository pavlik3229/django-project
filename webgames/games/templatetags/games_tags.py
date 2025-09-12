from django import template
from ..utils import fields
register = template.Library()

@register.inclusion_tag('games/wheel.html')
def show_wheel():
    return {'fields': fields}