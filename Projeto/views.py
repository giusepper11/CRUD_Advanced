from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def lerdoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Joaquim', 'idade': 27}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0}


def article(request, year):
    return HttpResponse('O ano passado é {}'.format(year))


def fname2(request, nome):
    idade = lerdoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})
