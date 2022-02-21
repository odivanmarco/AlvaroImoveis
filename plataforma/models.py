from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

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
               ('A', 'Aluguel'))

    choices_imovel = (('A', 'Apartamento'),
                      ('C', 'Casa'),('L','Lote'))
                      
    codigo_imovel = models.IntegerField(unique=True)
    imagens = models.ManyToManyField(Imagem)
    valor = models.FloatField()
    quartos = models.IntegerField()
    tamanho = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    rua = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=choices)
    tipo_imovel = models.CharField(max_length=1, choices=choices_imovel)
    numero = models.IntegerField()
    descricao = models.TextField()
   

    def __str__(self) -> str:
        return self.rua