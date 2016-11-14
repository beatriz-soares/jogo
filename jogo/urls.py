from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^instrucoes/$', views.instrucoes, name='instrucoes'),
    url(r'^jogar/(?P<id>\d+)/$', views.jogo, name='jogo'),

]