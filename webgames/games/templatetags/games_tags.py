from django import template
from ..utils import fields, fields_in_order
register = template.Library()

# @register.inclusion_tag('games/_wheel_board.html')
# def show_wheel_and_board():
#     return {
#         'fields': fields,
#         'fields_in_order': fields_in_order,
#     }