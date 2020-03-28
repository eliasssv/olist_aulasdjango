from django.db import models
from django.utils import timezone

class Endereco(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    deletado_em = models.DateTimeField(blank=True)
    logradouro = models.TextField(max_length=500)
    numero = models.TextField(max_length=10)
    bairro = models.TextField(max_length=50)
    cidade = models.TextField(max_length=100)
    uf = models.TextField(max_length=2)

    def delete(self):
        deletado_em = timezone.now()
        self.save()

    class Meta:
        abstract = True

class EnderecoRemetente(Endereco):
    nome_remetente = models.TextField(max_length=200)

class EnderecoDestinatario(Endereco):
    nome_destinatario = models.TextField(max_length=200)
    
class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    slug = models.CharField(max_length=500)