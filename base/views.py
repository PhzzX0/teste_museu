from django.shortcuts import render

# Create your views here.

def base(request):
    '''essa  funcao esta trabalhando com a requisicao da pagina e a gente tem que tratar essa requisicao'''
    return render(request, 'base/home.html')

def visitar(request):
    return render(request, 'base/visitar.html')

def museu(request):
    return render(request, 'base/museu.html')

def acervo(request):
    return render(request, 'base/acervo.html')

def CHCTPLA(request):
    return render(request, 'base/CHCTPLA.html')