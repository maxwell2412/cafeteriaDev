from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Cafe
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

def clientes(request):
    if request.method == 'GET':
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_list})
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
    
def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    
    cliente = Cliente.objects.filter(id=id_cliente)
    cafe = Cafe.objects.filter(cliente=cliente[0])
    
    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    cafe_json = json.loads(serializers.serialize('json', cafe))
    print(cafe_json)
    
    cafe_json = [{'fields': peds['fields'], 'id': peds['pk']}  for peds in cafe_json]

    data = {'cliente': cliente_json, 'cafe':cafe_json}
    #print(data)
    
    return JsonResponse(data)
@csrf_exempt
def update_cafe(request, id):
    nome_cafe = request.POST.get('pedido')
    tamanho = request.POST.get('tamanho')
    mesa = request.POST.get('mesa')
    
    return HttpResponse(nome_cafe)