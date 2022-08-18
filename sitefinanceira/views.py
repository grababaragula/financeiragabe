from django.shortcuts import render
from sitefinanceira.models import Beneficios,Recursos,Precos

def index(request):
    print(request)
    print(f'Metodo:{request.method}')
    print(f'headers:{request.headers}')
    print(f"User-agent:{request.headers['User-Agent']}")
    print(f'User:{request.user}')

    if str(request.user) == 'AnonymousUser':
        teste = 'usuario nao esta logado'
    else:
        teste = 'usuario esta logado'

    context ={
        'curso': 'programacao web django',
        'outro':'flamengo',
        'logado': teste,
    }

    return render(request, 'index.html',context)

def recursos(request):
    data = { }
    data['db'] = Recursos.objects.all()

    return render(request, 'recursos.html',data)

def beneficios(request):
    data = { }
    data['db'] = Beneficios.objects.all()

    return render(request, 'beneficios.html',data)

def precos(request):
    data = { }
    data['db'] = Precos.objects.all()

    return render(request, 'precos.html',data)