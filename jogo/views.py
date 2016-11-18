# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.from django.http import HttpResponse

# Página principal retorna o HTML do menu
def index(request):
    return render(request, "jogo/menu.html")


def instrucoes(request):
    return render(request, "jogo/instrucoes.html")

# A função jogo define a quantidade de discos nos postes
def jogo(request, id):
    if id == '1':
        qtd = 3
    elif id == '2':
        qtd = 5
    elif id == '3':
        qtd = 7
    else:
        qtd = 1
    return render(request, "jogo/jogo.html", locals())

def sair(request):
    return render(request, "jogo/saida.html")
