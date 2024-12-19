from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='home'),  # URL raiz do app base
]