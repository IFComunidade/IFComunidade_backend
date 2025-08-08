from django.db import models
from .tipo_setor import TipoSetor

class Setor(models.Model):
    tipo_setor = models.ForeignKey(TipoSetor, on_delete=models.PROTECT, related_name="setores")
    nome = models.CharField(max_length=120)
    horario_funcionamento = models.CharField(max_length=50, blank=True, null=True)
    sigla = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.nome ({self.sigla})}"