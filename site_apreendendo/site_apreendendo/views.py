from django.http import HttpResponse
from django.shortcuts import render

def paginaMain(request):
    return HttpResponse("Estou tentando novamente...")

def cadastroEstudante(request):
    return render(request,'Index_cadastro.html')