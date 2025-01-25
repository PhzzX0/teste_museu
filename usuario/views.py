from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def usuario_login(request):
    return render(request, 'usuario/login.html') # View para a página de login


def usuario_cadastro(request):
    return render(request, 'usuario/cadastro.html')  # View para a página de cadastro

def agendar_visita(request):
    return render(request, 'usuario/agendarvisita.html') # view pra a página agendar visita

