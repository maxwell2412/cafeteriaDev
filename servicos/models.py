from django.db import models
from clientes.models import Cliente
class Servico(models.Model):
	titulo = models.CharField(max_length=30)
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	