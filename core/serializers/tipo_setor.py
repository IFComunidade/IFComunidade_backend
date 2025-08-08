from rest_framework.serializers import ModelSerializer
from core.models import TipoSetor

class TipoSetorSerializer(ModelSerializer):
    class Meta:
        model = TipoSetor
        fields = '__all__'