from django import template
from main.models import *

register = template.Library()


# @register.simple_tag()
# def menu_tag():
#     return Menu.objects.all()

@register.inclusion_tag('main/menu_tpl.html')
def show_menu():
    my_menu = Menu.objects.all()
    return {'my_menu': my_menu}
