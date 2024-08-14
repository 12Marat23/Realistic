from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def get_menu(request, slug):
    return render(request, 'main/index.html')
