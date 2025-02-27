from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario, Agendamento  # Certifique-se de importar os modelos Usuario e Agendamento

def usuario_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        print(f"E-mail recebido: {email}")  # Depuração
        print(f"Senha recebida: {senha}")   # Depuração

        user = Usuario.objects.filter(email=email).first()
        if not user:
            print("Usuário não encontrado")  # Depuração
            messages.error(request, "Usuário não encontrado com esse e-mail.")
            return render(request, 'usuario/login.html')

        if check_password(senha, user.senha):
            print("Senha correta")  # Depuração
            messages.success(request, "Login bem-sucedido!")
            return redirect('agendar_visita')
        else:
            print("Senha incorreta")  # Depuração
            messages.error(request, "Senha incorreta. Tente novamente.")
            return render(request, 'usuario/login.html')

    return render(request, 'usuario/login.html')



def usuario_cadastro(request):
    if request.method == 'POST':  
        # Capturando os dados do formulário
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')


        # Validação: Verificar se o e-mail já está cadastrado
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "O e-mail já está em uso. Tente outro.")
            return redirect('usuario_cadastro')  # Redireciona para o formulário novamente

        # Criar um novo usuário e salvar no banco de dados
        Usuario.objects.create(
            nome_completo=nome_completo,
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
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        tipo_visitante = request.POST.get('tipo_visitante')
        instituicao = request.POST.get('instituicao', None)  # Pode ser vazio
        quantidade_visitantes = request.POST.get('quantidade_visitantes')
        data = request.POST.get('data')
        horario = request.POST.get('horario')

        # Se for "Instituição", o nome da instituição será obrigatório
        if tipo_visitante == 'instituicao' and not instituicao:
            messages.error(request, "Por favor, forneça o nome da instituição.")
            return render(request, 'usuario/agendarvisita.html')

        # Criar o agendamento e salvar no banco
        Agendamento.objects.create(
            nome_completo=nome_completo,
            email=email,
            telefone=telefone,
            tipo_visitante=tipo_visitante,
            instituicao=instituicao if tipo_visitante == 'instituicao' else None,
            quantidade_visitantes=quantidade_visitantes,
            data=data,
            horario=horario
        )

        messages.success(request, f"Agendamento para {nome_completo} no dia {data} às {horario} realizado com sucesso!")
        return redirect('agendar_visita')  # Redireciona para a página inicial ou onde você desejar após o agendamento

    return render(request, 'usuario/agendarvisita.html')
