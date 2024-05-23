from django.shortcuts import render, redirect
from .models import Cla

# Crie uma view para listar os clãs existentes
def list_clas(request):
    clãs = Cla.objects.all()  # Obtém todos os clãs do banco de dados
    return render(request, 'clas.html', {'clãs': clãs})

# View para redirecionar para a página de listagem de clãs
def redirect_to_list_clas(request):
    return redirect('list_clas')

