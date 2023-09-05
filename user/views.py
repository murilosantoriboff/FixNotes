from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User # Criar o Cadastro
from django.contrib.auth import authenticate # Autenticar Login
from django.contrib.auth.decorators import login_required # Permissão de login para areas diversas do sistema


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Não existem dados o suficiente no formulario')
            return redirect('/user/login/')
        
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'user/cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Não existem dados o suficiente no formulario')
            return redirect('/user/cadastro/')
        else:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                messages.add_message(request, constants.SUCCESS, 'Sucesso ao cadastrar Usuario')
                return redirect('/user/login/')
            except:
                messages.add_message(request, constants.ERROR, 'Erro na Hora de Cadastrar')
                return redirect('/user/cadastro/')