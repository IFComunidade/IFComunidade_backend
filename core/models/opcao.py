from django.db import models
from .postagem import Postagem

class Opcao(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name="postagem")
    titulo = models.CharField(max_length=120)
    quantidade_votos = models.IntegerField
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Opção"
        verbose_name_plural = "Opções"