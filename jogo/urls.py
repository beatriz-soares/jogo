# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views
#Aqui definimos as urls que vamos usar para cada página, que serão chamadas pelas funções que estão na views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^instrucoes/$', views.instrucoes, name='instrucoes'),
    url(r'^nomear_jogadores/$', views.nomear_jogadores, name='nomear_jogadores'),
    url(r'^jogo/$', views.jogo, name='jogo'),
    url(r'^transicao/(?P<pontos>\d+)/$', views.transicao, name='transicao'),

]
