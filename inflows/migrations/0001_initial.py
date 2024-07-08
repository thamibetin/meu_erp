# Generated by Django 5.0.6 on 2024-07-07 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contacts", "0001_initial"),
        (
            "produtos",
            "0005_alter_produto_options_rename_lenght_produto_length_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Inflows",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Observações"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="inflows",
                        to="produtos.produto",
                        verbose_name="Produto",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="inflows",
                        to="contacts.contact",
                        verbose_name="Fornecedor",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
