# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Página principal retorna o HTML do menu
def index(request):
    return render(request, "jogo/menu.html")


def instrucoes(request):
    return render(request, "jogo/instrucoes.html")

def nomear_jogadores(request):
    """Guarda os nomes de todos jogadores que existirem (um ou dois) na sessão, e define a quantidade
    de jogos a serem jogados. Se tiver um jogador, então a quantidade de jogos a serem jogados será 1,
    por exemplo.
    """
    request.session['jogos_pendentes'] = 0
    # Salva os nomes dos jogadores na sessao
    if request.method == 'POST':
        if 'nome_jogador1' in request.POST:
            request.session['nome_jogador1'] = request.POST['nome_jogador1']
            request.session['jogos_pendentes'] += 1
        if 'nome_jogador2' in request.POST:
            request.session['nome_jogador2'] = request.POST['nome_jogador2']
            request.session['jogos_pendentes'] += 1

        request.session['jogador_da_vez'] = request.POST['nome_jogador1']

        return HttpResponseRedirect(reverse('jogo'))

    range_nomes = range(request.session['numero_jogadores'])

    return render(request, "jogo/coletar_nomes_jogadores.html", locals())

def configuracoes_do_modal(request):
    """No modal de escolher o nivel de dificuldade do jogo, existe um formulario que vai dizer
    qual a dificuldade o jogador escolheu e se ele escolheu multiplayer. Esta view trabalha essas
    informações.
    """
    if request.method == 'POST':
        # Define a quantidade de discos nos postes
        # Detectar a dificuldade do jogo. O padrão é o nível fácil:
        if 'nivel1' in request.POST:
            request.session['qtd'] = 3
            request.session['peso_tempo'] = 1
            request.session['peso_jogadas'] = 1
        elif 'nivel2' in request.POST:
            request.session['qtd'] = 5
            request.session['peso_tempo'] = 0.02
            request.session['peso_jogadas'] = 0.02
        elif 'nivel3' in request.POST:
            request.session['qtd'] = 7
            request.session['peso_tempo'] =0.01
            request.session['peso_jogadas'] = 0.01
        else:
            request.session['qtd'] = 3
            request.session['peso_tempo'] = 1
            request.session['peso_jogadas'] = 1

        # Detectar o modo de jogo. O tamanho da lista declarada abaixo é
        # a quantidade de nomes a serem perguntados na template.
        if 'gamemode' in request.POST:
            request.session['numero_jogadores'] = 1
        else:
            request.session['numero_jogadores'] = 2

        return HttpResponseRedirect(reverse('nomear_jogadores'))
    return render(request, "jogo/menu.html")

def jogo(request):
    return render(request, "jogo/jogo.html", locals())

def transicao(request, pontos):
    """Faz o seguinte:
    Se tiver dois jogadores, troca o turno
    Diminui o numero de jogos que ainda devem ser jogados
    Se nao faltar mais nenhum jogo, manda pra tela final
    Se ainda faltar jogo, manda pra tela de jogo
    """
    if request.session['jogador_da_vez'] == request.session['nome_jogador1']:
        request.session['pontuacao_jogador1'] = pontos
        if 'nome_jogador2' in request.session:
            request.session['jogador_da_vez'] = request.session['nome_jogador2']

    else:
        request.session['pontuacao_jogador2'] = pontos
        request.session['jogador_da_vez'] = request.session['nome_jogador1']

    request.session['jogos_pendentes'] -= 1

    if request.session['jogos_pendentes'] > 0:
        return render(request, "jogo/jogo.html", locals())
    else:
        return render(request, "jogo/transicao.html", locals())

def sair_do_jogo(request):
    """Apaga todos dados guardados na sessão, inclusive os nomes dos jogadores, pontuação etc
    Redireciona para pagina do google!
    """
    request.session.flush()
    return HttpResponseRedirect('https://www.google.com.br/')

def resetar_sessao(request):
    """Apaga todos dados guardados na sessão, inclusive os nomes dos jogadores, pontuação etc
    Redireciona para pagina principal!
    """
    request.session.flush()
    return HttpResponseRedirect(reverse('index'))

def recomecar_jogo(request):
    """Depois da tela de fim de jogo, o jogador pode escolher jogar novamente, mantendo os jogadores
    mas mudando o nivel de dificuldade. Esta view seta o nivel de dificuldade e reseta a variavel
    'jogos_pendentes'.
    """
    if request.method == 'POST':
        if 'nivel1' in request.POST:
            request.session['qtd'] = 3
            request.session['peso_tempo'] = 1
            request.session['peso_jogadas'] = 1
        elif 'nivel2' in request.POST:
            request.session['qtd'] = 5
            request.session['peso_tempo'] = 0.002
            request.session['peso_jogadas'] = 0.002
        elif 'nivel3' in request.POST:
            request.session['qtd'] = 7
            request.session['peso_tempo'] =0.001
            request.session['peso_jogadas'] = 0.001
        else:
            request.session['qtd'] = 3
            request.session['peso_tempo'] = 1
            request.session['peso_jogadas'] = 1

        request.session['jogos_pendentes'] = request.session['numero_jogadores']

        return render(request, "jogo/jogo.html", locals())
    return resetar_sessao(request)
