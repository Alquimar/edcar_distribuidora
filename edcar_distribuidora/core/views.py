from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Departamento, Categoria, Item

def quem_somos(request):
    template_name = "core/quem_somos.html"
    context = {}
    return render(request, template_name, context)


def contato(request):
    template_name = "core/contato.html"
    context = {}
    return render(request, template_name, context)


def home(request):
    departamentos = Departamento.objects.filter(ativo=True)
    produtos = Item.objects.filter(ativo=True)
    template_name = "core/home.html"
    context = {
        'departamentos': departamentos,
        'produtos': produtos
    }
    return render(request, template_name, context)


def itens_categoria(request, categoria_id):
    departamentos = Departamento.objects.filter(categorias__isnull=False, ativo=True).distinct()
    produtos = Item.objects.filter(categoria_id=categoria_id)
    template_name = "core/itens_categoria.html"
    categoria = Categoria.objects.get(pk=categoria_id)
    context = {
        'departamentos': departamentos,
        'produtos': produtos,
        'categoria': categoria
    }
    return render(request, template_name, context)