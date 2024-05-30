
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Personagem
from .forms import PersonagemForm

# View para a página inicial
def home(request):
    # Renderiza a página inicial
    return render(request, 'personagens/home.html')

# View para listar todos os personagens
def personagem_list(request):
    # Obtém todos os objetos Personagem
    personagens = Personagem.objects.all()
    context = {
        'personagens': personagens,  # Corrigido de 'personagem' para 'personagens'
        'title': 'Lista de Personagens'
    }
    # Renderiza a lista de personagens
    return render(request, 'personagens/personagens_list.html', context)

# View para os detalhes de um personagem específico
def personagem_detail(request, pk):
    # Obtém o objeto Personagem com a chave primária (pk) fornecida, ou retorna um 404 se não for encontrado
    personagens = get_object_or_404(Personagem, pk=pk)  # Corrigido de 'personagem' para 'Personagem'
    context = {
        'personagem': personagens,
        # Usando a notação de ponto simples para acessar o nome do livro
        'title': f'Detalhes do Personagem: {personagens.nome} - {personagens.livro.nome}'  # Corrigido 'livro__nome' para 'livro.nome'
    }
    # Renderiza os detalhes do personagem
    return render(request, 'personagens/personagens_detail.html', context)

# View para adicionar um novo personagem
def personagem_novo(request):
    if request.method == 'POST':
        # Cria um formulário com os dados submetidos
        form = PersonagemForm(request.POST, request.FILES)
        if form.is_valid():
            # Salva o novo personagem se o formulário for válido
            novo_personagem = form.save()
            # Redireciona para os detalhes do novo personagem
            return redirect('personagem_detail', pk=novo_personagem.pk)  # Corrigido de 'cla_detail' para 'personagem_detail'
    else:
        # Cria um formulário vazio se a requisição não for POST
        form = PersonagemForm()
    
    context = {
        'form': form,
        'title': 'Adicionar novo Personagem'
    }
    # Renderiza a página de criação de personagem com o formulário
    return render(request, 'personagens/personagens_form.html', context)  # Corrigido caminho do template
