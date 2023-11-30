from django.urls import path 
from . import views

#novas urls com base na requisição do cliente por Request/response
urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('atualiza_cliente/', views.att_cliente, name="atualiza_cliente"),
    path('update_cafe/<int:id>', views.update_cafe, name="update_cafe"),
    path('excluir_cafe/<int:id>', views.excluir_cafe, name="excluir_cafe"),
    path('update_cliente/<int:id>', views.update_cliente, name="update_cliente")
    
]
