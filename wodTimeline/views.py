from django.shortcuts import render, redirect

def home(request):
    """
    View para renderizar a página inicial do projeto.
    """
    return render(request, "home.html")

