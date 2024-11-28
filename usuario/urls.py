from django.urls import path
from . import views

urlpatterns = [
    # Exemplo de rota
    path('', views.index, name='usuario'),
]
