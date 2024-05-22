from django.urls import path
from . import views


urlpatterns = [
    path('clas/', views.clas_lista, ),
]

