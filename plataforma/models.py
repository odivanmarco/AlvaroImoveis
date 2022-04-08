from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, EmailField, IntegerField

class Imagem(models.Model):
    img = models.ImageField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url

class Cidade(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome

class Imovei(models.Model):
    choices = (('V', 'Venda'),
               ('A', 'Aluguel'),('T','Temporada'))

    choices_imovel = (('A', 'Apartamento'),
                      ('C', 'Casa'),('L','Lote'),('IC','Imóvel_Comercial'),('IR','Imóvel_Rural'))
                        
    imagens = models.ManyToManyField(Imagem)
    valor = models.FloatField()
    quartos = models.IntegerField()
    tamanho = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=60)
    tipo = models.CharField(max_length=1, choices=choices)
    tipo_imovel = models.CharField(max_length=2, choices=choices_imovel)
    numero = models.IntegerField()
    descricao = models.TextField()
    garagens = models.IntegerField()
    banheiros = models.IntegerField()
   

    def __str__(self) -> str:
        return self.rua
        
class Contato(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField()
    def __str__(self) :
        return self.name