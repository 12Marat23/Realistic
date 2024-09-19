from django.shortcuts import render
from django.views.generic import ListView
from main.models import *


# Create your views here.

class HomeListView(ListView):
    model = Article
    template_name = 'main/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        # Получаем последние 6 статей, отсортированных по времени создания
        return Article.objects.order_by('-id')[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        articles = context['articles']
        grouped_articles = [articles[i:i + 3] for i in range(0, len(articles), 3)]
        context['grouped_articles'] = grouped_articles
        return context


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
