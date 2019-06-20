from django.forms import ModelForm
from .models import Estudante

class EstudanteForm(ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome','sobreNome','idade','telefone','cidade','email']