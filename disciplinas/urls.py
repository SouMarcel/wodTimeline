from . import views
from django.urls import path

urlpatterns = [
    path('lista/', views.disciplina_list, name="disciplina_list"),
    path('disciplina/<int:pk>/', views.disciplina_detail, name='disciplina_detail'),
    path('disciplina_novo/', views.disciplina_create, name='disciplina_create'),
    path('', views.home, name="home"),
]
