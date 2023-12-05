from django.db import models
from clientes.models import Cliente
from .choices import ChoiceCategoriaAdicao
class CategoriaAdicao():
	titulo = models.CharField(max_length=3, choices=ChoiceCategoriaAdicao.choices)
	preco = models.DecimalField(max_digits=8, decimal_places=2)
	
	def __str__(self):
		return self.titulo
class Servico(models.Model):
	titulo = models.CharField(max_length=30)
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	
	categoria_adicao = models.ManyToManyField(CategoriaAdicao)
	
	data_inicio = models.DateField(null=True)
	hora_entrega = models.DateTimeField(null=True)
	finalizado = models.BooleanField(default=False)
	protecolo = models.CharField(max_length=32, null=True, blank=True)