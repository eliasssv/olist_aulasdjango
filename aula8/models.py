from django.db import models

class Pet(models.Model):
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField(null=True)
    ativo = models.BooleanField(default=True, help_text="ativo ou inativo")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Animau"
        verbose_name_plural = "Animaus"