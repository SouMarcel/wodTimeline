from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.local_list, name='local_list'),
]
