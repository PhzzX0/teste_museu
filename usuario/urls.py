from django.urls import path
from . import views

# urlpatterns contém a lista de roteamentos de URLs

#path(rota, view, kwargs=None, name='')

# ● rota: string contendo a rota (URL).
# ● view: a função (ou classe) que irá tratar essa rota.
# ● kwargs: utilizado para passar dados adicionais à função ou método que irá tratar a requisição.
# ● name: nome da rota. O Django utiliza o app_name mais o nome da rota para nomear a URL

urlpatterns = [
   

    path('login/', views.usuario_login, name='usuario_login'),
    path('cadastro/', views.usuario_cadastro, name='usuario_cadastro'),
    path('agendar_visita/', views.agendar_visita, name='agendar_visita'),
]
