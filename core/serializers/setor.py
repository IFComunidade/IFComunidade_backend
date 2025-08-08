from rest_framework.serializers import ModelSerializer
from .setor import Setor

class SetorSerializer(ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'