from django.urls import path
from . import views

urlpatterns = [
    path('', views.livros_ls, name="livros_ls"), 
]
