from django.contrib.auth.models import AnonymousUser
from rest_framework.viewsets import ModelViewSet
from core.models import Ocorrencia
from core.serializers import OcorrenciaSerializer
from usuario.models import Usuario

class OcorrenciaViewSet(ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer

    def get_queryset(self):
        usuario: Usuario = self.request.user
        if usuario.tipo == Usuario.TipoUser.ALUNO:
            return Ocorrencia.objects.filter(usuario=usuario)
        if Ocorrencia.setor == Usuario.tipo:
            return Ocorrencia.objects.filter(usuario=usuario)