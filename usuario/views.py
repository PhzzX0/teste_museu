from django.shortcuts import render

# Create your views here.

def base(request):
    '''essa  funcao esta trabalhando com a requisicao da pagina e a gente tem que tratar essa requisicao'''
    return render(request, 'usuario/usuario.html')
