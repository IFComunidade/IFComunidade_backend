from rest_framework.serializers import ModelSerializer
from usuario.serializers import UsuarioSerializer
from core.models import Tramite

class TramiteSerializer(ModelSerializer):
    
    autor = UsuarioSerializer(read_only=True)
    
    class Meta:
        model = Tramite
        fields = '__all__'