from django.contrib import admin

from .models import Loja, Catalogo, Departamento, Categoria, Item


class LojaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo']
    search_fields = ['nome']
    list_filter = ['ativo', 'criado_em']


class CatalogoAdmin(admin.ModelAdmin):
    list_display = ['loja', 'nome', 'ativo']
    search_fields = ['loja', 'nome']
    list_filter = ['loja', 'ativo', 'criado_em']
    fields = ['loja', 'nome']


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo']
    search_fields = ['nome']
    list_filter = ['ativo', 'criado_em']


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['departamento', 'nome', 'ativo']
    search_fields = ['nome']
    list_filter = ['ativo', 'criado_em']
    fields = ['departamento', 'nome']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['catalogo', 'categoria', 'nome', 'valor']
    search_fields = ['nome']
    list_filter = ['categoria', 'ativo', 'criado_em']
    fields = ['categoria', 'catalogo', 'nome', 'codigo', 'valor', 'descricao', 'mostrar_valor', 'imagem']

admin.site.register(Loja, LojaAdmin)
admin.site.register(Catalogo, CatalogoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Item, ItemAdmin)