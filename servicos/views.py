from django.shortcuts import render, get_object_or_404
from .forms import FormServico
from django.http import HttpResponse, FileResponse
from .models import Servico
from fpdf import FPDF
from io import BytesIO
def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Salvo com sucesso!")
        else:
            return render(request, 'novo_servico.html', {'form': form})
    
def lista_servico(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        return render(request, 'lista_servico.html', {'servicos': servicos})
        #return render(request, 'lista_servico.html')
    
def servico(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador )
    return render(request, 'servico.html', {'servico': servico})

def gerar_os(request, identificador):
    servico = get_object_or_404(Servico, identificador=identificador)
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 10)

    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, 'Ordem de serviço', 1, 1, 'C', 1)
    pdf.cell(0, 10, 'CafeteriaDev', 1, 1, 'C', 1)

    pdf.cell(35, 10, 'Cliente: ', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.cliente.nome}', 1, 1, 'L', 1)
    
    categorias_adicao = servico.categoria_adicao.all()

    pdf.cell(35, 10, 'Adições: ', 1, 0, 'L', 1)
    for i, add in enumerate(categorias_adicao):
        pdf.cell(0, 10, f'- {add.get_titulo_display()}', 1, 1, 'L', 1)
        if not i == len(categorias_adicao) -1:
            pdf.cell(35, 10, '', 0, 0)

        pdf.cell(35, 10, 'Data de inicio: ', 1, 0, 'L', 1)
        pdf.cell(0, 10, f'{servico.data_inicio}', 1, 1, 'L', 1)

        pdf.cell(35, 10, 'Hora de entrega: ', 1, 0, 'L', 1)
        pdf.cell(0, 10, f'{servico.hora_entrega}', 1, 1, 'L', 1)

        pdf.cell(35, 10, 'Protocolo: ', 1, 0, 'L', 1)
        pdf.cell(0, 10, f'{servico.protecolo}', 1, 1, 'L', 1)

        pdf.cell(35, 10, 'Preço total: ', 1, 0, 'L', 1)
        pdf.cell(0, 10, f' R$ {servico.preco_total()}', 1, 1, 'L', 1)

    pdf_content = pdf.output(dest='S').encode('latin1') #salvando em memoria codificado em latim
    pdf_bytes = BytesIO(pdf_content)
    return FileResponse(pdf_bytes, as_attachment=True, filename=f"os-{servico.protecolo}.pdf")
   