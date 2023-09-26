from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Categoria, Nota
from django.contrib.messages import constants
from django.contrib import messages

# Trabalhar no form de criar notas

@login_required(login_url='/user/login/')
def home(request):
    notas = Nota.objects.all()
    return render(request, 'notes/home.html', {'notas':notas})

@login_required(login_url='/user/login/')
def nova_categoria(request):
    if request.method == 'GET':
        return render(request, 'notes/nova_categoria.html')
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        cat = Categoria.objects.create(titulo=titulo, descricao=descricao)
        cat.save()
        messages.add_message(request, messages.constants.SUCCESS, 'Categoria Criada')
        return redirect('/home/')
    
@login_required(login_url='/user/login/')
def nova_nota(request):
    pass