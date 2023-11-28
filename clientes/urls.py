from django.urls import path 
from . import views

#novas urls com base na requisição do cliente por Request/response
urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('atualiza_cliente/', views.att_cliente, name="atualiza_cliente")
    
]
