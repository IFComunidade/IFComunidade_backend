from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.models import Postagem
from core.serializers import PostagemSerializer
from rest_framework.exceptions import PermissionDenied
from usuario.models import Usuario
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Postagem"])
class PostagemViewSet(ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    
    def perform_create(self, serializer):
        usuario: Usuario = self.request.user  # type: ignore

        if not isinstance(usuario, Usuario):
            raise PermissionDenied("Usuário inválido ou não autenticado.")
        
        if usuario.tipo != Usuario.TipoUser.SETOR:
            raise PermissionDenied("Só setores devem criar postagens.")

        serializer.save(usuario=usuario)
        
    def get_permissions(self):
        if self.action in ['list', 'retrieve']: 
            return [AllowAny()]
        return [IsAuthenticated()]
