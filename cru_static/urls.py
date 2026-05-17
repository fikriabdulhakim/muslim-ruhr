from django.urls import path
from core.views import home, about, articles, article_detail, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('articles/', articles, name='articles'),
    path('articles/<slug:slug>/', article_detail, name='article_detail'),
    path('contact/', contact, name='contact'),
]
