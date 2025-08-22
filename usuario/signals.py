from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.usuario import Aluno, Setor
from .models.perfil import PerfilAluno, PerfilSetor 

@receiver(post_save, sender=Aluno)
def create_aluno_profile(sender, instance, created, **kwargs):
    if created and instance.tipo == "ALUNO":
        PerfilAluno.objects.create(usuario=instance)

@receiver(post_save, sender=Setor)
def create_setor_profile(sender, instance, created, **kwargs):
    if created and instance.tipo == "SETOR":
        PerfilSetor.objects.create(usuario=instance)