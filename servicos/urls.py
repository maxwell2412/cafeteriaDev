from django.urls import path 
from . import views

#novas urls com base na requisição do cliente por Request/response
urlpatterns = [
    path('novo_servico/', views.novo_servico, name="novo_servico"),
    path('lista_servico/', views.lista_servico, name="lista_servico"),
    path('servico/<str:identificador>/', views.servico, name="servico"),
    path('gerar_os/<str:identificador>/', views.gerar_os, name="gerar_os"),
]
