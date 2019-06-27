from django.urls import path
from .views import cadastroEstudante


urlpatterns = [
   path("Cadastro/",cadastroEstudante,name="cadastro"),

]