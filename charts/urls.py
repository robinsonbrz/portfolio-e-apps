from django import views
from django.urls import path

from . import views

app_name = 'cotacoes'
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home, name='home'),
    # path('delta/<par_moedas>/<int:dias>', views.home, name='home'),

]
