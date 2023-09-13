from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#Fazer o Log out futuramente

# Fazer a interface para mostrar se ele possui notas ou nao, com as funções de criar categoria de notas e dentro dessas categorias criar notas, além de notas fora da categoria.

@login_required(login_url='/user/login/')
def home(request):
    return render(request, 'notes/home.html')