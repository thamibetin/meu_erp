from django.db import models
from contacts.models import Contact
from produtos.models import Produto

class Inflows(models.Model):
    supplier = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='inflows', verbose_name='Fornecedor')
    product = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='inflows', verbose_name='Produto')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True, verbose_name='Observações')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
    

