from django.shortcuts import render
from .forms import FormServico

def novo_servico(request):
    form = FormServico()
    return render(request, 'novo_servico.html', {'form': form})