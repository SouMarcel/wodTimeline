from django.shortcuts import render, redirect, get_object_or_404
from .models import Local
from .forms import LocalForm

# Cria suas views aqui.
def home(request):  # Define a view chamada "home"
    return render(request, 'locais/home.html')  # Renderiza o template 'home.html' na pasta 'locais'

# View para listagem de locais
def local_list(request):  # Define a view chamada "local_list" para listar os locais
    local = Local.objects.all()  # Atribui à variável 'local' todos os itens da tabela 'Local'
    
    context = {  # Cria um dicionário de contexto para passar ao template
        'local': local,  # Passa a variável 'local' (todos os itens da tabela 'Local') para o template
        'title': 'Lista de locais'  # Passa uma string 'Lista de locais' como título da página
    }
    return render(request, 'locais/locais_list.html', context)  # Renderiza o template 'locais_list.html' na pasta 'locais' com as variáveis do contexto

def local_novo(request):  # Define a view para adicionar um novo local
    if request.method == 'POST':  # Verifica se o método da requisição é POST
        form = LocalForm(request.POST)  # Instancia o formulário com os dados enviados
        if form.is_valid():  # Verifica se o formulário é válido
            novo_local = form.save()  # Salva os dados do formulário no banco de dados
            if request.POST.get('action') == 'save_and_add_new':
                return redirect('local_novo')
            return redirect('local_detail', pk=novo_local.pk)  # Redireciona para a detalhes da nova entrada
    else:  # Se o método da requisição não for POST
        form = LocalForm()  # Instancia um formulário vazio
    
    context = {  # Cria o dicionário de contexto para passar ao template
        'form': form,  # Passa o formulário para o template
        'title': 'Adicionar novo Local'  # Passa o título da página para o template
    }
    return render(request, 'locais/locais_form.html', context)  # Renderiza o template com o contexto


def local_detail(request, pk):
    local = get_object_or_404(Local,pk=pk)
    context = {
        'local': local,
        'title': f'Detalhes do Local: {local.nome} - {local.livro}'
    }
    return render(request, 'locais/locais_detail.html', context)