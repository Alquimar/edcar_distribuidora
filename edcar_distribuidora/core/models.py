from django.db import models

class AbstractModel(models.Model):
    nome = models.CharField('Nome', max_length=50,  unique=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    ativo = models.BooleanField('Ativo(a)?', default=True)

    class Meta:
        abstract = True


class Loja(AbstractModel):

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        verbose_name = "Loja"
        verbose_name_plural = "Lojas"


class Catalogo(AbstractModel):
    loja = models.ForeignKey(Loja, verbose_name='loja', related_name='catalogos', on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {}'.format(self.loja ,self.nome)

    class Meta:
        verbose_name = "Catálogo"
        verbose_name_plural = "Catálogos"


class Departamento(AbstractModel):

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"


class Categoria(AbstractModel):
    departamento = models.ForeignKey(Departamento, verbose_name='departamento', related_name='categorias', on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Item(AbstractModel):
    categoria = models.ForeignKey(Categoria, verbose_name='categoria', related_name='itens', on_delete=models.PROTECT)
    catalogo = models.ForeignKey(Catalogo, verbose_name='catalogo', related_name='itens', on_delete=models.PROTECT)
    codigo = models.BigIntegerField('Código', unique=True)
    descricao = models.TextField('Descrição')
    valor = models.DecimalField('Valor (R$)', max_digits=10, decimal_places=2)
    mostrar_valor = models.BooleanField('Mostrar valor no catálogo?', default=False)
    imagem = models.ImageField(upload_to='item/imagens', verbose_name='Imagem',
                               null=True, blank=True)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.catalogo, self.categoria.departamento, self.categoria, self.nome)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"