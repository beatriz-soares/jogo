# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# saida
# Precisamos deixar a sessão zerada na saída!!.
# if 'qtd' in request.session:
#     del request.session['qtd']
# if 'jogador1' in request.session:
#     del request.session['jogador1']
# if 'jogador2' in request.session:
#     del request.session['jogador2']


# Página principal retorna o HTML do menu
def index(request):
    return render(request, "jogo/menu.html")


def instrucoes(request):
    return render(request, "jogo/instrucoes.html")

def jogo(request):
    # Define a quantidade de discos nos postes
    # Detectar a dificuldade do jogo. O padrão é o nível fácil:
    if 'nivel1' in request.POST:
        request.session['qtd'] = 3
    elif 'nivel2' in request.POST:
        request.session['qtd'] = 5
    elif 'nivel3' in request.POST:
        request.session['qtd'] = 7
    else:
        request.session['qtd'] = 3

    # Detectar o modo de jogo. O tamanho da lista declarada abaixo é
    # a quantidade de nomes a serem perguntados na template.
    if 'gamemode' in request.POST:
        range_nomes = [1]
    else:
        range_nomes = [1,2]

    return render(request, "jogo/coletar_nomes_jogadores.html", locals())

def transicao(request, pontos):
    pontos = pontos
    return render(request, "jogo/transicao.html", {'pontos':pontos})
