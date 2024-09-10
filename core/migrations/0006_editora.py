# Generated by Django 5.0.6 on 2024-09-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_livro"),
    ]

    operations = [
        migrations.CreateModel(
            name="Editora",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("site", models.URLField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
