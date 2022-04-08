
from django.urls import path, re_path

from . import views

app_name = 'portapp'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('expertise/', views.expertise, name='expertise'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contato/', views.contato, name='contato'),
    re_path(r'ajxmail/$', views.ajxmail, name='ajxmail'),
]
