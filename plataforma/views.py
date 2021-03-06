from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Imovei,Cidade,Contato

# Create your views here.

def sobre(request):
    return render(request, 'sobre.html')

def financiamento(request):
    return render(request, 'financiamento.html')

def faleconosco(request):
    if request.method=="GET":
        return render(request, 'faleconosco.html')
    else:
        contact = Contato()
        name = request.POST.get('name')
        email = request.POST.get('emailC')
        telefone = request.POST.get('telefone')
        subject = request.POST.get('mensagem')
        contact.name = name
        contact.email = email
        contact.telefone = telefone
        contact.mensagem = subject
        contact.save()
        mensagem = "Mensagem enviada com sucesso"
        return render(request,'faleconosco.html',{'mensagem': mensagem})


def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')
    tipoAV = request.GET.getlist('tipoAV')
    cidades = Cidade.objects.all()
    if preco_minimo or preco_maximo or cidade or tipo or tipoAV:
        
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999
        if not tipo:
            tipo = ['A', 'C', 'L']
        if not tipoAV:
            tipoAV = ['A', 'V']
        
        
        imoveis = Imovei.objects.filter(valor__gte=preco_minimo)\
        .filter(valor__lte=preco_maximo)\
        .filter(tipo_imovel__in=tipo).filter(cidade=cidade)\
        .filter(tipo__in=tipoAV).filter(cidade=cidade)
    else:
        imoveis = Imovei.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})

def buscaPorCodigo(request):
    id = request.GET.get('id')
    imovel = Imovei.objects.filter(id=id)
    return render(request, 'home.html', {'imoveis': imovel})

def imovel(request, id):
    imovel = get_object_or_404(Imovei, id=id)
    sugestoes = Imovei.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    return render(request, 'imovel.html', {'imovel': imovel, 'sugestoes': sugestoes, 'id': id})

def  aluguelOuVenda(request):
    tipoAV = request.GET.get('tipoAV')
    cidades = Cidade.objects.all()
    imoveis = Imovei.objects.filter(tipo__in=tipoAV)
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})

