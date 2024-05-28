

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Disciplina
from .forms import DisciplinaForm


# home
def home(request):
    return render(request, 'disciplinas/home.html')


# View para listar todas as disciplinas
def disciplina_list(request):
    disciplinas = Disciplina.objects.all()
    context = {
        'disciplinas': disciplinas,
        'title': 'Lista de Disciplinas'
    }
    return render(request, 'disciplinas/disciplina_list.html', context)

# View para mostrar os detralhes da disciplina
def disciplina_detail(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    context = {
        'disciplina': disciplina,
        'title': f'Detalhes da Disciplina: {disciplina.nome}'
    }
    return render(request, 'disciplinas/disciplina_detail.html', context)

# adicionar uma nova disciplina
def disciplina_create(request):
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(disciplina_list)
    else:
        form = DisciplinaForm()
    context = {
        'form': form,
        'title': 'Adicionar nova Disciplina'
    }
    return render(request, 'disciplinas/disciplina_form.html', context)