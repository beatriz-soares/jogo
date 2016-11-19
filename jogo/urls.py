# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views
#Aqui definimos as urls que vamos usar para cada página, que serão chamadas pelas funções que estão na views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^instrucoes/$', views.instrucoes, name='instrucoes'),
    url(r'^jogar/(?P<id>\d+)/$', views.jogo, name='jogo'),
    url(r'^transicao/(?P<pontos>\d+)/$', views.transicao, name='transicao'),

]