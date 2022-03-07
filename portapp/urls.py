
from django.urls import path

from . import views

urlpatterns = [
    path('', views.port_index, name='port_index'),
]
