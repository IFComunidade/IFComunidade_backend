from rest_framework.serializers import ModelSerializer
from .tipo_setor import TipoSetor

class TipoSetorSerializer(ModelSerializer):
    class Meta:
        model = TipoSetor
        fields = '__all__'