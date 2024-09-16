from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('<str:slug>/', get_menu, name='menu'),

    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('blog/', blog, name='blog'),
    path('gallery/', gallery, name='gallery'),
]