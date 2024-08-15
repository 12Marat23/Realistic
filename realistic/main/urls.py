from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<str:slug>/', get_menu, name='menu'),
]