from django.shortcuts import render

# Create your views here.
"""
# notacao 1
def livros_ls(request):
    livros_ls = livros.objects.all()
    return render(request, 'livros/livros_ls.html', {'livros_ls': livros_ls})
    """

# notação 2
def livros_ls(request):
    livros_ls = livros.objects.all()
    context = {
        'livros_ls': livros_ls, # conteudo da model livros
        'title': 'Lista de Personagens' # gera ima variavel chamda title que pode ser chamada diretamente no tamplate
    }
    return render(request, 'livros/lista.html', context)