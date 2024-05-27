# livros/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Livro, Edicao
from .forms import LivroForm, EdicaoForm

# View to list all books
def livro_list(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros,
        'title': 'Lista de Livros'
    }
    return render(request, 'livros/livro_list.html', context)

# View to see the details of a single book
def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    context = {
        'livro': livro,
        'title': f'Detalhes do Livro: {livro.nome}'
    }
    return render(request, 'livros/livro_detail.html', context)

# View to add a new book
def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_list')
    else:
        form = LivroForm()
    context = {
        'form': form,
        'title': 'Adicionar Novo Livro'
    }
    return render(request, 'livros/livro_form.html', context)

#### Views for `Edicao`

# View to list all editions
def edicao_list(request):
    edicoes = Edicao.objects.all()
    context = {
        'edicoes': edicoes,
        'title': 'Lista de Edições'
    }
    return render(request, 'livros/edicao_list.html', context)

# View to see the details of a single edition
def edicao_detail(request, pk):
    edicao = get_object_or_404(Edicao, pk=pk)
    context = {
        'edicao': edicao,
        'title': f'Detalhes da Edição: {edicao.nome}'
    }
    return render(request, 'livros/edicao_detail.html', context)

# View to add a new edition
def edicao_create(request):
    if request.method == 'POST':
        form = EdicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edicao_list')
    else:
        form = EdicaoForm()
    context = {
        'form': form,
        'title': 'Adicionar Nova Edição'
    }
    return render(request, 'livros/edicao_form.html', context)
