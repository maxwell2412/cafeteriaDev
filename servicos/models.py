from django.db import models
from clientes.models import Cliente
from .choices import ChoiceCategoriaAdicao
from datetime import datetime
from secrets import token_hex

class CategoriaAdicao(models.Model):
	titulo = models.CharField(max_length=3, choices=ChoiceCategoriaAdicao.choices)
	preco = models.DecimalField(max_digits=8, decimal_places=2)
	
	def __str__(self) -> str:
		return self.titulo
class Servico(models.Model):
	titulo = models.CharField(max_length=30)
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	
	categoria_adicao = models.ManyToManyField(CategoriaAdicao)
	
	data_inicio = models.DateField(null=True)
	hora_entrega = models.DateTimeField(null=True)
	finalizado = models.BooleanField(default=False)
	protecolo = models.CharField(max_length=52, null=True, blank=True)
 
	def __str__(self) -> str:
		return self.titulo


	def save(self, *args, **kwargs):
		if not self.protecolo:
			self.protecolo = datetime.now().strftime("%D/%M/%Y-%H/%M/%S-") + token_hex(16)
         
		super(Servico, self).save(*args, **kwargs)

	def preco_total(self):
		preco_total = float(0)
		for categoria in self.categoria_adicao.all():
			preco_total += float(categoria.preco)

		return preco_total

     