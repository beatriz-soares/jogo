# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.from django.http import HttpResponse

# Página principal retorna o HTML do menu
def index(request):
    return render(request, "jogo/menu.html")


def instrucoes(request):
    return render(request, "jogo/instrucoes.html")

# A função jogo define a quantidade de discos nos postes
def jogo(request):
    # Detectar a dificuldade do jogo. O padrão é fácil:
    if 'nivel1' in request.POST:
        qtd = 3
    elif 'nivel2' in request.POST:
        qtd = 5
    elif 'nivel3' in request.POST:
        qtd = 7
    else:
        qtd = 3

    # Detectar o modo de jogo.
    if 'gamemode' in request.POST:
        gamemode = 'singleplayer'
    else:
        gamemode = 'multiplayer'
        
    return render(request, "jogo/jogo.html", locals())

def transicao(request, pontos):
    pontos = pontos
    return render(request, "jogo/transicao.html", {'pontos':pontos})
