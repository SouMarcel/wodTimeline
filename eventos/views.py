from django.shortcuts import render

# Create your views here.
def lista(request):
    return render(request, 'lista.html')
