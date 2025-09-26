from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from core.models import Curso
from core.serializers import CursoSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Curso"])
class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer