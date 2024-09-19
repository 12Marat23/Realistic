from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('blog/', blog, name='blog'),
    path('gallery/', gallery, name='gallery'),
]