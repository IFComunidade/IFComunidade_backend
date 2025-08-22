from rest_framework.viewsets import ModelViewSet
from core.models import Ocorrencia
from core.serializers import OcorrenciaSerializer
from rest_framework.permissions import IsAuthenticated

class OcorrenciaViewSet(ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer

    permission_classes = [IsAuthenticated]