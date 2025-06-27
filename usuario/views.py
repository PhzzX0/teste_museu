from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario, Agendamento  

def usuario_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Usuario.objects.filter(email=email).first()
        if not user:
            messages.error(request, "Usuário não encontrado com esse e-mail.")
            return render(request, 'usuario/login.html')

        print(f"Senha digitada: {senha}")  # Depuração
        print(f"Senha armazenada (hash): {user.senha}")  # Depuração

        if check_password(senha, user.senha):  # Senha deve estar criptografada no banco
            request.session['usuario_id'] = user.id
            messages.success(request, "Login bem-sucedido!")
            return redirect('agendar_visita')
        else:
            messages.error(request, "Senha incorreta. Tente novamente.")
            return render(request, 'usuario/login.html')

    return render(request, 'usuario/login.html')



def usuario_cadastro(request):
    if request.method == 'POST':  
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "O e-mail já está em uso. Tente outro.")
            return redirect('usuario_cadastro')

        try:
            usuario = Usuario.objects.create(
                nome_completo=nome_completo,
                email=email,
                senha=make_password(senha)  # Senha deve ser criptografada
            )
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso! Você pode fazer login agora.')
            return redirect('usuario_login')
        except Exception as e:
            messages.error(request, f"Erro ao cadastrar usuário: {str(e)}")
            return redirect('usuario_cadastro')

    return render(request, 'usuario/cadastro.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Agendamento

def agendar_visita(request):
    usuario_id = request.session.get('usuario_id')  
    if not usuario_id:
        messages.error(request, "Você precisa estar logado para agendar uma visita.")
        return redirect('usuario_login')

    usuario = Usuario.objects.get(id=usuario_id)

    if request.method == 'POST':
        telefone = request.POST.get('telefone')
        tipo_visitante = request.POST.get('tipo_visitante')
        instituicao = request.POST.get('instituicao', None)
        quantidade = request.POST.get('quantidade_visitantes', 1)
        data = request.POST.get('data')
        horario = request.POST.get('horario')

        # Se for individual, define automaticamente a quantidade como 1
        if tipo_visitante == 'individual':
            quantidade = 1

        Agendamento.objects.create(
            usuario=usuario,
            telefone=telefone,
            tipo_visitante=tipo_visitante,
            instituicao=instituicao if tipo_visitante == 'instituicao' else None,
            quantidade_visitantes=quantidade,
            data=data,
            horario=horario
        )

        messages.success(request, f"Agendamento para {usuario.nome_completo} no dia {data} às {horario} realizado com sucesso!")
        return redirect('agendar_visita')

    return render(request, 'usuario/agendarvisita.html')
