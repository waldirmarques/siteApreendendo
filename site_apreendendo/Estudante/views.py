from django.shortcuts import render, redirect
from .models import Estudante
from .forms import EstudanteForm


def cadastroEstudante(request):


    form = EstudanteForm(request.FILES, request.POST or None)

    if(request.method == 'POST'):

        nome = request.POST.get('nome_cad')
        sobreNome = request.POST.get('sobrenome_cad')
        idade = request.POST.get('idade_cad')
        telefone = request.POST.get('telefone_cad')
        cidade = request.POST.get('cidade_cad')
        email = request.POST.get('email_cad')

        # Criando estudante
        myEstudante = Estudante(nome=nome,sobreNome=sobreNome,idade=idade,telefone=telefone,cidade=cidade,email=email)

        myEstudante.save_base()

        return redirect('/.') #redireciona para a página principal do site...

    return render(request,'cadastro/Index_cadastro.html',{'form':form})
