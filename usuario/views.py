from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Usuario  # Certifique-se de importar o modelo Usuario

def usuario_login(request):
    if request.method == 'POST':
        # Pegando os dados do formulário
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        # Tentando buscar o usuário no banco de dados (por nome ou sobrenome)
        try:
            # Aqui procuramos o usuário, levando em consideração o nome e sobrenome juntos
            user = Usuario.objects.get(nome=nome)  # ou nome e sobrenome, dependendo de como você quer fazer
        except Usuario.DoesNotExist:
            messages.error(request, "Usuário não encontrado.")
            return render(request, 'usuario/login.html')

        # Verificando se a senha fornecida é correta
        if check_password(senha, user.senha):
            messages.success(request, "Login bem-sucedido!")
            return redirect('homepage')  # Redirecionar para a página inicial ou outra página de sucesso
        else:
            messages.error(request, "Senha incorreta. Tente novamente.")
            return render(request, 'usuario/login.html')

    return render(request, 'usuario/login.html')  # Caso o método não seja POST, apenas renderiza o formulário de login

def usuario_cadastro(request):
    if request.method == 'POST':  # Corrigido a indentação aqui
        # Capturando os dados do formulário
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('Sobrenome')
        name_user = request.POST.get('name_user')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Validação: Verificar se as senhas coincidem
        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem. Tente novamente.")
            return redirect('usuario_cadastro')  # Redireciona para o formulário novamente

        # Validação: Verificar se o e-mail já está cadastrado
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "O e-mail já está em uso. Tente outro.")
            return redirect('usuario_cadastro')  # Redireciona para o formulário novamente

        # Criar um novo usuário e salvar no banco de dados
        Usuario.objects.create(
            nome=nome,
            sobrenome=sobrenome,
            name_user=name_user,
            email=email,
            senha=make_password(senha)  # Salvando a senha de forma segura
        )

        messages.success(request, 'Cadastro realizado com sucesso! Você pode fazer login agora.')
        return redirect('usuario_login')  # Redireciona para a página de login após o cadastro

    # Renderizar o formulário para GET
    return render(request, 'usuario/cadastro.html')


def agendar_visita(request):
    if request.method == 'POST':
        # Pegando os dados do formulário
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        tipo_visitante = request.POST.get('tipo_visitante')
        instituicao = request.POST.get('instituicao', None)  # Pode ser vazio
        data = request.POST.get('data')
        horario = request.POST.get('horario')

        # Criar o agendamento e salvar no banco
        agendamento = Agendamento.objects.create(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            telefone=telefone,
            tipo_visitante=tipo_visitante,
            instituicao=instituicao,
            data=data,
            horario=horario
        )

        return HttpResponse(f"Agendamento para {nome} {sobrenome} no dia {data} às {horario} realizado com sucesso!")

    return render(request, 'usuario/agendarvisita.html')  # Caso não seja POST, apenas renderiza o formulário de agendamento
