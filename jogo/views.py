# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

# saida
# Precisamos deixar a sessao zerada na saída!!.
# if 'qtd' in request.session:
#     del request.session['qtd']
# if 'jogador1' in request.session:
#     del request.session['jogador1']
# if 'jogador2' in request.session:
#     del request.session['jogador2']


# Página principal retorna o HTML do menu
def index(request):

    if request.method == 'POST':
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
            request.session['numero_jogadores'] = 1
        else:
            request.session['numero_jogadores'] = 2

        return HttpResponseRedirect(reverse('nomear_jogadores'))
    return render(request, "jogo/menu.html")


def instrucoes(request):
    return render(request, "jogo/instrucoes.html")

def nomear_jogadores(request):
    # Guarda-se na sessao a quantidade de jogos que ainda faltam. Serve para
    # dizer se ainda falta algum jogador participar.
    request.session['jogos_pendentes'] = 0
    print '*********************'
    print 'Jogadores nomeados:'
    # Salva os nomes dos jogadores na sessao
    if request.method == 'POST':
        if 'nome_jogador1' in request.POST:
            request.session['nome_jogador1'] = request.POST['nome_jogador1']
            request.session['jogos_pendentes'] += 1
            print request.session['nome_jogador1']
        if 'nome_jogador2' in request.POST:
            request.session['nome_jogador2'] = request.POST['nome_jogador2']
            request.session['jogos_pendentes'] += 1
            print request.session['nome_jogador2']

        request.session['jogador_da_vez'] = request.POST['nome_jogador1']

        print "Serão jogados ", request.session['jogos_pendentes'],' jogos'
        print "Jogador da vez será ", request.session['jogador_da_vez']
        return HttpResponseRedirect(reverse('jogo'))

    range_nomes = range(request.session['numero_jogadores'])

    return render(request, "jogo/coletar_nomes_jogadores.html", locals())

def jogo(request):
    return render(request, "jogo/jogo.html", locals())

def transicao(request, pontos):
    # Atribui a pontuação ao jogador da vez na sessao e muda o jogador da vez
    if 'jogador_da_vez' in request.session:
        if request.session['jogador_da_vez'] == request.session['nome_jogador1']:
            request.session['pontos_jogador1'] = pontos
            if 'nome_jogador2' in request.session:
                request.session['jogador_da_vez'] = request.session['nome_jogador2']
        else:
            request.session['pontos_jogador2'] = pontos
            request.session['jogador_da_vez'] = request.session['nome_jogador1']

        # Atualiza a quantidade de jogos que ainda serao jogados.
        request.session['jogos_pendentes'] -= 1


        # Decide se manda pra tela de jogo de novo ou se manda pra tela de resultado
        # final.
        if request.session['jogos_pendentes'] > 0:
            return render(request, "jogo/jogo.html", locals())
        return render(request, "jogo/transicao.html", locals())
    else:
        return HttpResponse("Nao sei quem joga agora!")
