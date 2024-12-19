from django.shortcuts import render

def usuario_login(request):
    return render(request, 'usuario/login.html')

def usuario_cadastro(request):
    return render(request, 'usuario/cadastro.html')  # View para a página de cadastro
