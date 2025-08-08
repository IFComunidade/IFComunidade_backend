from rest_framework.serializers import ModelSerializer
from .models import TipoSetor

class TipoSetorSerializer(ModelSerializer):
    class Meta:
        model = TipoSetor
        fields = '__all__'