from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='home_page'),  # URL raiz do app base
    path('visitar/', views.visitar, name='visitar'),  # URL para a página visitar
    path('museu/', views.museu, name='museu'),  # URL para a página museu
    path('acervo/', views.acervo, name='acervo'),  # URL para a página acervo
    path('CHCTPLA/', views.CHCTPLA, name='CHCTPLA'),  # URL para a página CHCTPLA
]