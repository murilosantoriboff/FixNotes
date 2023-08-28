from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        return HttpResponse('Enviado login')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'user/cadastro.html')
    elif request.method == 'POST':
        return HttpResponse('Enviado cadastro')
