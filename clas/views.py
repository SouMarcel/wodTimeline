from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import Cla
from .forms import ClaForm

# Create your views here.
# home
def home(request):
    return render(request, 'clas/home.html')


# View para listar todas as cla
def cla_list(request):
    cla = Cla.objects.all()
    context = {
        'cla': cla,
        'title': 'Lista de clas'
    }
    return render(request, 'clas/cla_list.html', context)

# View para mostrar os detralhes da cla
def cla_detail(request, pk):
    cla = get_object_or_404(Cla, pk=pk)
    context = {
        'cla': cla,
        'title': f'Detalhes do Cla: {cla.nome}'
    }
    return render(request, 'clas/cla_detail.html', context)

# adicionar uma nova disciplina
def cla_create(request):
    if request.method == "POST":
        form = ClaForm(request.POST)
        if form.is_valid():
            # form.save()
            # return redirect(cla_detail)
            novo_cla = form.save()
            return redirect('cla_detail', pk=novo_cla.pk)  # Redireciona para os detalhes do novo clã
    else:
        form = ClaForm()
    context = {
        'form': form,
        'title': 'Adicionar novo Cla'
    }
    return render(request, 'clas/cla_form.html', context)