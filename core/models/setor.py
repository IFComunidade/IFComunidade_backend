from django.db import models

class Setor(models.Model):
    nome = models.CharField(max_length=120)
    horario_funcionamento = models.CharField(max_length=50, blank=True, null=True)
    sigla = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.nome} ({self.sigla})"
    
    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"