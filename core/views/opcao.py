from rest_framework.viewsets import ModelViewSet
from core.models import Opcao
from core.serializers import OpcaoSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Opção"])
class OpcaoViewSet(ModelViewSet):
    queryset = Opcao.objects.all()
    serializer_class = OpcaoSerializer