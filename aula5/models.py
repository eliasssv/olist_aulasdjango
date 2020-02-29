from django.db import models
from django.db.models import Sum

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    twitter = models.URLField()
    data_nascimento = models.DateField(null=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.TextField()
    categorias = models.ManyToManyField(Categoria, related_name="posts")
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    autor = models.CharField(max_length=30)
    comentario = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.autor} no post {self.post}"

class Carrinho(models.Model):
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.data)

    @property
    def valor_total(self):
        return self.produtos.aggregate(Sum('valor'))

class Produto(models.Model):
    descricao = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="produtos")

    def __str__(self):
        return f"{self.descricao} - {self.valor}"

