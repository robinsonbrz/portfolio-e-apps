
from django.urls import re_path

from . import views

app_name = 'portapp'
urlpatterns = [
    re_path('', views.inicio, name='inicio'),
    re_path('about/', views.about, name='about'),
    re_path('expertise/', views.expertise, name='expertise'),
    re_path('portfolio/', views.portfolio, name='portfolio'),
    re_path('contato/', views.contato, name='contato'),
    re_path(r'enviaemail/$', views.enviaemail, name='enviaemail'),
]
