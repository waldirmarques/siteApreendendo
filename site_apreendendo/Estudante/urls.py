from django.urls import path
from .views import cadastroEstudante, paginaHome


urlpatterns = [
   path("Cadastro/",cadastroEstudante,name="cadastro"),
   path("Home/",paginaHome,name="home")
]