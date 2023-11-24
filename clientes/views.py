from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Cafe
import re
def clientes(request):
    if request.method == 'GET':
        return render(request, 'clientes.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        pedido = request.POST.getlist('pedido')
        tamanho = request.POST.getlist('tamanho')
        mesa = request.POST.getlist('mesa')
        cliente = Cliente.objects.filter(cpf=cpf)
        if cliente.exists():
            return render(request, 'clientes.html', {'nome':nome, 'sobrenome':sobrenome, 'email':email, 'pedido': zip(pedido, tamanho, mesa)})
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clientes.html', {'nome':nome, 'sobrenome':sobrenome, 'cpf':cpf, 'pedido': zip(pedido, tamanho, mesa)})
         
        cliente = Cliente(
        nome = nome,
        sobrenome = sobrenome,
        email = email,
        cpf = cpf
        )
        
        cliente.save()
        
        for pedido, tamanho, mesa in zip(pedido, tamanho, mesa):
            coffee = Cafe(pedido=pedido, tamanho=tamanho, mesa=mesa, cliente=cliente)
            coffee.save()
        return HttpResponse('Teste')