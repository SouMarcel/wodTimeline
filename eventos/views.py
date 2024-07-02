# eventos/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import EventoForm

def home(request):
    return render(request, 'eventos/home.html')


def lista(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista.html', {'eventos': eventos})


def detalhe(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos/detalhe.html', {'evento': evento})


def novo(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()  # Salva o evento no banco de dados
            return redirect('detalhe', pk=evento.pk)  # Redireciona para a página de detalhes do novo evento criado
    else:
        form = EventoForm()
    return render(request, 'eventos/novo.html', {'form': form})


def edit_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    
    if request.method == 'POST':
        if 'editar' in request.POST:  # Verifica se o formulário de edição foi submetido
            form = EventoForm(request.POST, instance=evento)
            if form.is_valid():
                form.save()  # Salva as alterações no evento existente
                return redirect('detalhe', pk=evento.pk)  # Redireciona para a página de detalhes do evento editado
        elif 'excluir' in request.POST:  # Verifica se o formulário de exclusão foi submetido
            evento.delete()  # Exclui o evento do banco de dados
            return redirect('lista')  # Redireciona para a lista de eventos após exclusão
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'eventos/edit_delete.html', {'form': form, 'evento': evento})