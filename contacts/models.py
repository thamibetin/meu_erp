from django.db import models
from contact_types.models import ContactTypes


class Contact(models.Model):
    name = models.CharField(max_length=500)
    full_name = models.CharField(max_length=500)
    contact_type = models.ForeignKey(ContactTypes, on_delete=models.PROTECT, verbose_name='Tipo de contato', null=True, blank=True)
    document = models.CharField(max_length=20, verbose_name='CPF/CNPJ')
    telephone = models.CharField(max_length=20, verbose_name='Telefone', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='e-mail')
    limit_credit = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name='Limite de Crédito')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    

