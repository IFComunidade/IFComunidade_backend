from rest_framework.viewsets import ModelViewSet
from core.models import Tramite, Ocorrencia
from core.serializers import TramiteSerializer
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
@extend_schema(tags=["Trâmite"])
class TramiteViewSet(ModelViewSet):
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer

    def perform_create(self, serializer):
        ocorrencia_id = self.request.data.get('ocorrencia') # type: ignore
        ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)

        if ocorrencia.status in [
            Ocorrencia.Status.CONCLUIDO_NAO_RESOLVIDO,
            Ocorrencia.Status.CONCLUIDO_RESOLVIDO,
        ]:  
            raise PermissionDenied("A ocorrência já foi finalizada, não é possível registrar mais trâmites")