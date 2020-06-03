from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Categoria, Item

def getTodos(request):
    categorias = Categoria.objects.filter(itens__isnull=False, ativo=True).distinct()
    template_name = "core/home.html"
    context = {
        'categorias': categorias
    }
    return render(request, template_name, context)


def getItensCategoria(request, categoria_id):
    categorias = Categoria.objects.filter(itens__isnull=False, ativo=True).distinct()
    itens = Item.objects.filter(categoria_id=categoria_id)
    template_name = "core/itens_categoria.html"
    categoria_id = categoria_id
    context = {
        'categorias': categorias,
        'itens': itens,
        'categoria_id': categoria_id
    }
    return render(request, template_name, context)