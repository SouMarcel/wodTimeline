from django.shortcuts import render, redirect
from . models import clas

# Create your views here.
#Cris a view para listar os clas existentes
def clas(request):
    return redirect('clas/clas')