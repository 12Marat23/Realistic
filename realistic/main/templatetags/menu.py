from django import template
from main.models import *

register = template.Library()


@register.inclusion_tag('main/menu_tpl.html')
def get_menu():
    menus = Menu.objects.order_by('-name')
    return {'menus': menus}
