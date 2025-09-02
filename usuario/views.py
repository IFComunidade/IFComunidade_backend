from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()