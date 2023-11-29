from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=11)
    
    def __str__(self) -> str:
        return self.nome

class Cafe(models.Model):
    pedido =  models.CharField(max_length=50)
    tamanho = models.CharField(max_length=3)
    mesa = models.IntegerField()
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.pedido 
