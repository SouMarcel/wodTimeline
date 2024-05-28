from . import views
from django.urls import path

urlpatterns = [
    path('lista/', views.cla_list, name="cla_list"),
    path('cla/<int:pk>', views.cla_detail, name="cla_detail"),
    path('cla_novo', views.cla_create, name="cla_create"),
    path('', views.home, name="home")
]
