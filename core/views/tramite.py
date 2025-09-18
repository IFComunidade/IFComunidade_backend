from rest_framework.viewsets import ModelViewSet
from core.models import Tramite, Ocorrencia
from core.serializers import TramiteSerializer
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from usuario.models import Usuario

@extend_schema(tags=["Trâmite"])
class TramiteViewSet(ModelViewSet):
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer

    def get_queryset(self):
        usuario: Usuario = self.request.user
        ocorrencia_id = self.request.query_params.get('ocorrencia_id')

        queryset = Tramite.objects.all()

        if ocorrencia_id:
            queryset = queryset.filter(ocorrencia__id=ocorrencia_id)

        if usuario.tipo == Usuario.TipoUser.ALUNO:
            queryset = queryset.filter(ocorrencia__usuario=usuario)
        elif usuario.tipo == Usuario.TipoUser.SETOR:
            queryset = queryset.filter(ocorrencia__setor=usuario)
        else:
            return Tramite.objects.none()
        
        return queryset

    def perform_create(self, serializer):
        usuario: Usuario = self.request.user
        ocorrencia_id = self.request.data.get('ocorrencia')
        ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)

        if ocorrencia.status in [
            Ocorrencia.Status.CONCLUIDO_NAO_RESOLVIDO,
            Ocorrencia.Status.CONCLUIDO_RESOLVIDO,
        ]:
            raise PermissionDenied("Não é possível registrar respostas em uma ocorrência finalizada.")

        if usuario.tipo == Usuario.TipoUser.ALUNO and ocorrencia.usuario != usuario:
            raise PermissionDenied("Você não pode registrar respostas em ocorrências de outros usuários.")
        elif usuario.tipo == Usuario.TipoUser.SETOR and ocorrencia.setor != usuario:
            raise PermissionDenied("Você não pode registrar respostas em ocorrências de outros setores.")

        serializer.save(autor=usuario, ocorrencia=ocorrencia)