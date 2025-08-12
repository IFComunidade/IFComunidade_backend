from rest_framework.viewsets import ModelViewSet
from core.models import Setor
from core.serializers import SetorSerializer

class SetorViewSet(ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer