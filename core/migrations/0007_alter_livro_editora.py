# Generated by Django 5.0.6 on 2024-09-10 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_editora"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="editora",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.editora",
            ),
        ),
    ]
