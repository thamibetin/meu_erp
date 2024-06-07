from django.db import models

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, blank=True, null=True, unique=True)
    name = models.CharField(max_length=200, verbose_name='Nome')
    unit = models.CharField(max_length=200, verbose_name='Unidade')
    origin = models.SmallIntegerField(verbose_name='Origem')
    ncm = models.CharField(max_length=10, verbose_name='NCM')
    cest = models.CharField(max_length=9, verbose_name='CEST', blank=True, null=True)
    price = models.FloatField(verbose_name='Preço de Venda')
    cost = models.FloatField(verbose_name='Preço de Custo', blank=True, null=True)
    stock = models.FloatField(verbose_name='Estoque', blank=True, null=True)
    ean = models.CharField(max_length=14, verbose_name='Código de barras EAN', blank=True, null=True)
    net_weight = models.FloatField(verbose_name='Peso Líquido', blank=True, null=True)
    gross_weight = models.FloatField(verbose_name='Peso Bruto', blank=True, null=True)
    lenght = models.FloatField(verbose_name='Comprimento do produto', blank=True, null=True)
    width = models.FloatField(verbose_name='Largura do produto', blank=True, null=True)
    height = models.FloatField(verbose_name='Altura do produto', blank=True, null=True)
    expire_day = models.DateField(verbose_name='Data de Validade', blank=True, null=True)
    description = models.TextField(max_length=2000, verbose_name='Descrição Principal', blank=True, null=True)
    short_description = models.TextField(max_length=2000, verbose_name='Descrição Complementar', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)







