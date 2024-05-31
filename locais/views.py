from django.shortcuts import render
from .models import Local

# Create your views here.
def home(request):
    return render(request, 'locais/home.html')

# view para listagem de local
def local_list(request):
    local = Local.objects.all() # variavel local = a todos os itens na tabela Local
    
    context = { # cria a variavel para passar 2 outras variaveis
        'local': local, # variavel que sera passada ao html referente a tabela Local
        'title': 'Lista de locais'  # variavel com um nome para a pagina
    }
    return render(request, 'locais/locais_list.html', context) # retorna a pagina de listagem e as variaveis no contexto


def local_novo(request):
    if request.method == 'POST':
        form = LocalForm(request.POST) 