from rest_framework.viewsets import ModelViewSet
from core.models import Opcao
from core.serializers import OpcaoSerializer

class OpcaoViewSet(ModelViewSet):
    queryset = Opcao.objects.all()
    serializer_class = OpcaoSerializer