from django.db import models

class Person(models.Model):
    nome = models.CharField(max_length=50)
    sobreNome = models.CharField(max_length=50)
    fomacao = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.IntegerField()
    email = models.EmailField(max_length=200)

    #função que coloca o nome da Parson cadastrada no django admim
    def __str__(self):
        return self.nome



