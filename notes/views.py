from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Categoria, Nota

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
        return HttpResponse('Deu Certo')