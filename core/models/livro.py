from django.db import models

from .editora import Editora


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100, blank=True, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
