from django.db import models
from core.models import Ocorrencia
from usuario.models import Usuario

class Tramite(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE, related_name="respostas")
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="respostas")
    data = models.DateTimeField(auto_now_add=True)
    resposta = models.TextField()

    def __str__(self):
        return f"Trâmite feito por {self.autor}"