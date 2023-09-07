from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#Fazer o Log out futuramente

@login_required(login_url='/user/login/')
def home(request):
    return HttpResponse('Home')