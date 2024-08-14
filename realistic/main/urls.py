from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('menu/<str:slug>', get_menu, name='menu')
]