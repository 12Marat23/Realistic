from django.shortcuts import render
from django.views.generic import ListView
from main.models import Menu


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def get_menu(request, slug):
    return render(request, 'main/_menu.html')
