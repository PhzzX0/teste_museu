from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.usuario_login, name='usuario_login'),
    path('cadastro/', views.usuario_cadastro, name='usuario_cadastro'),  # Nova URL para o cadastro
]
