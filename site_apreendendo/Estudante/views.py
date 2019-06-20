from django.shortcuts import render, redirect
from .models import Estudante
from .forms import EstudanteForm

def paginaHome(request):
    banco = Estudante.objects.all()
    return render(request, "Home/home.html", {'Estudante': banco})

def cadastroEstudante(request):


    form = EstudanteForm(request.FILES, request.POST or None)

    if(request.method == 'POST'):

        nome = request.POST.get('nome_cad')
        print("Esse valor é: ",nome)
        sobreNome = request.POST.get('sobrenome_cad')
        idade = request.POST.get('idade_cad')
        telefone = request.POST.get('telefone_cad')
        cidade = request.POST.get('cidade_cad')
        email = request.POST.get('email_cad')

        # Criando o usuario Aurora
        myEstudante = Estudante(nome=nome,sobreNome=sobreNome,idade=idade,telefone=telefone,cidade=cidade,email=email)

        myEstudante.save_base()

        return redirect('home')

    return render(request,'cadastro/Index_cadastro.html',{'form':form})
