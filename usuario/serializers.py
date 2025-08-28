from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Usuario, Setor, Aluno

class UsuarioSerializer(ModelSerializer):
    confimar_senha = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ["id", "email", "nome", "password", "confirmar_senha"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class SetorSerializer(ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'