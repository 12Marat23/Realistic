from django.shortcuts import render
from django.views.generic import ListView
from main.models import Menu


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def blog(request):
    return render(request, 'main/blog.html')


def gallery(request):
    return render(request, 'main/gallery.html')

# def get_menu(request, slug):
#     return render(request, 'main/menu_tpl.html')
