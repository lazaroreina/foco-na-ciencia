from django.db.models import fields
from django.shortcuts import render
from django.forms import ModelForm
from .models import *


# Create your views here.

# Criando classes de formulários

class SecretariaForm(ModelForm):
    class Meta:
        model = Secretaria
        fields = [
            'titular', 'email', 'telefone',
        ]

class AreaInteresseForm(ModelForm):
    class Meta:
        model = AreaInteresse
        fields = [
            'descricao', 'secretaria_relacionada',
        ]

def board(request, template_name="board.html"):

    query = request.GET.get("busca")
    if query:
        filtro = PalavrasChave.objects.filter(descricao__icontains= query)
        questoes = Questao.objects.filter(palavraschave__in = filtro)
    else:
        questoes= Questao.objects.all()

    return render(request, template_name, {'questoes': questoes})
