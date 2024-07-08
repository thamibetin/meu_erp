from django.db import models
from category.models import Category
from brands.models import Brand


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, blank=True, null=True, unique=True)
    name = models.CharField(max_length=200, verbose_name='Nome')
    unit = models.CharField(max_length=200, verbose_name='Unidade')
    origin = models.SmallIntegerField(verbose_name='Origem')
    ncm = models.CharField(max_length=10, verbose_name='NCM')
    cest = models.CharField(max_length=9, verbose_name='CEST', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de Venda')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de Custo', blank=True, null=True)
    stock = models.IntegerField(default=0, verbose_name='Estoque')
    ean = models.CharField(max_length=14, verbose_name='Código de barras EAN', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products', verbose_name='Marca', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Categoria', blank=True, null=True)
    net_weight = models.FloatField(verbose_name='Peso Líquido', blank=True, null=True)
    gross_weight = models.FloatField(verbose_name='Peso Bruto', blank=True, null=True)
    length = models.FloatField(verbose_name='Comprimento do produto', blank=True, null=True)
    width = models.FloatField(verbose_name='Largura do produto', blank=True, null=True)
    height = models.FloatField(verbose_name='Altura do produto', blank=True, null=True)
    expire_day = models.DateField(verbose_name='Data de Validade', blank=True, null=True)
    description = models.TextField(max_length=2000, verbose_name='Descrição Principal', blank=True, null=True)
    short_description = models.TextField(max_length=2000, verbose_name='Descrição Complementar', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    







