from django.shortcuts import render
from .models import Local

# Create your views here.
def home(request):
    return render(request, 'locais/home.html')

def local_list(request):
    local = Local.objects.all()
    
    context = {
        'local': local,
        'title': 'Lista de locais'
    }
    return render(request, 'locais/locais_list.html', context)


