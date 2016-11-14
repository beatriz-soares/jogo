# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.from django.http import HttpResponse

# Página principal retorna o HTML do menu
def index(request):
    return render(request, "jogo/menu.html")


def instrucoes(request):
    return render(request, "jogo/instrucoes.html")

# A função jogo retorna htmls diferentes dependendo do nível que o usuário escolheu
def jogo(request, id):
    if id == '1':
        return render(request, "jogo/nivel_1.html")
    elif id == '2':
        return render(request, "jogo/nivel_2.html")
    elif id == '3':
        return render(request, "jogo/nivel_3.html")
    else:
        return render(request, "jogo/menu.html")
