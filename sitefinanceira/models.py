from django.db import models

class Beneficios(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Porcentagem', decimal_places=2, max_digits=8)

    def __str__(self):
     return self.nome

class Recursos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    proposta = models.CharField('proposta', max_length=100)

    def __str__(self):
     return self.nome

class Precos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    def __str__(self):
     return self.nome