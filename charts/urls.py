from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'cotacoes'
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home, name='home'),
    # path('delta/<par_moedas>/<int:dias>', views.home, name='home'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
