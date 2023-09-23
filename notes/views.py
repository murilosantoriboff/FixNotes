from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Categoria, Nota

#Fazer o Log out futuramente

# Trabalhar no form de criar notas

@login_required(login_url='/user/login/')
def home(request):
    notas = Nota.objects.all()
    return render(request, 'notes/home.html', {'notas':notas})