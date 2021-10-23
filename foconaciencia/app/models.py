from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.deletion import CASCADE


# Criação de classes dos campos de bancos de dados


class Usuario(models.Model):
    nome = models.CharField(max_length= 50)
    email = models.EmailField()
    tel = models.CharField(max_length= 11)
        
    def __str__(self):
        return self.nome

class Secretaria(models.Model):
    nome = models.CharField(max_length= 30)
    titular = models.CharField(max_length= 30)
    email = models.EmailField()
    telefone = models.CharField(max_length= 11)

    def __str__(self):
        return self.nome

class AreaInteresse(models.Model):
    descricao = models.CharField(max_length=50)
    secretaria_relacionada = models.ForeignKey(Secretaria, on_delete= CASCADE)

    def __str__(self):
            return self.descricao

class Sugestoes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE)
    area_interesse = models.ForeignKey(AreaInteresse, on_delete= CASCADE)
    sugestao = models.TextField()

    class Meta:
        verbose_name_plural = "Sugestões"

class Links(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
            return self.descricao

    class Meta:
        verbose_name_plural = "Links"

class PalavrasChave(models.Model):
    descricao = models.CharField(max_length= 25)

    def __str__(self):
        return self.descricao

class Questao(models.Model):
    area_interesse = models.ForeignKey(AreaInteresse, on_delete= CASCADE)
    palavraschave = models.ManyToManyField(PalavrasChave)
    descricao = models.CharField(max_length= 100)
    resposta = models.TextField()
    links = models.ForeignKey(Links, on_delete= CASCADE)
    
    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Questões"








