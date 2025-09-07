from rest_framework.viewsets import ModelViewSet
from core.models import Categoria
from core.serializers import CategoriaSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Categoria"])
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer