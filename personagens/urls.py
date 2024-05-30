from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('lista/', views.personagem_list, name='personagens_list'),
    path('detail/<int:pk>/', views.personagem_detail, name='personagens_detail'),
    path('novo/', views.personagem_novo, name='personagem_novo')
    
]
