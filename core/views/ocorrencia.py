from rest_framework.viewsets import ModelViewSet
from core.models import Ocorrencia
from core.serializers import OcorrenciaSerializer

class OcorrenciaModelViewSet(ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer