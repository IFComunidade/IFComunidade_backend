from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Usuario, Setor, Aluno

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        
class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class SetorSerializer(ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'