from django import template
from main.models import *

register = template.Library()


@register.inclusion_tag('inc/_menu.html')
def menu_tag():
    menu = Menu.objects.order_by('id')
    return {'menu': menu}