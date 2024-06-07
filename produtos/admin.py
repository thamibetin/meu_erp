from django.contrib import admin
from produtos.models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('sku',
                    'name',
                    'unit',
                    'origin',
                    'price',
                    'cost',
                    'stock',
                    'ean',
                    'ncm',
                    'cest',
                    )
    search_fields = ('sku', 'name', 'ean',)

admin.site.register(Produto, ProdutoAdmin)
