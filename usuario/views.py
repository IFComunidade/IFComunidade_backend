from rest_framework.viewsets import ModelViewSet

from .models import Usuario, Aluno, Setor
from .serializers import UsuarioSerializer, AlunoSerializer, SetorSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class AlunoViewSet(ModelViewSet):
    queryset= Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class SetorViewSet(ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
