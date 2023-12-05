
from django.db.models import TextChoices

class ChoiceCategoriaAdicao(TextChoices):
	ADD_CHOCOLATE = "AC", "Adiciona Chocolate"
	ADD_OVOMALTINE = "AO", "Adiciona Ovomaltine"
	ADD_LEITE = "AL", "Adiciona Leite"
	ADD_AMENDOIM = "AM", "Adiciona Amendoim"