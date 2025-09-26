from django.contrib.auth.models import AnonymousUser
from rest_framework.viewsets import ModelViewSet
from core.models import Ocorrencia
from core.serializers import OcorrenciaSerializer
from usuario.models import Usuario
from rest_framework.exceptions import PermissionDenied
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Ocorrência"])
class OcorrenciaViewSet(ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer

    def get_queryset(self):
        usuario: Usuario = self.request.user # type: ignore
        if usuario.tipo == Usuario.TipoUser.ALUNO:
            return Ocorrencia.objects.filter(usuario=usuario)
        elif usuario.tipo == Usuario.TipoUser.SETOR:
            return Ocorrencia.objects.filter(setor=usuario)
        return Ocorrencia.objects.none()
    

    def perform_create(self, serializer):
        usuario: Usuario = self.request.user  # type: ignore

        if usuario.tipo != Usuario.TipoUser.ALUNO:
            raise PermissionDenied("Só alunos devem criar ocorrencias.")

        serializer.save(usuario=usuario)
