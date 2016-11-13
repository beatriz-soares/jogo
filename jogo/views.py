from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.from django.http import HttpResponse

def index(request):
    return render(request, "jogo/menu.html")

def instrucoes(request):
    return render(request, "jogo/instrucoes.html")


