from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.local_list, name='local_list'),
    path("novo/", views.local_novo, name="local_novo"),
    path('detalhes/<int:pk>', views.local_detail, name='local_detail')
]
