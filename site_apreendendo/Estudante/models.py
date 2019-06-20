from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=50)
    sobreNome = models.CharField(max_length=50)
    idade = models.IntegerField()
    telefone = models.IntegerField()
    cidade = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)

    #função que coloca o nome da Parson cadastrada no django admim
    def __str__(self):
        return self.nome



