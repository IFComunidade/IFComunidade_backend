from rest_framework.serializers import ModelSerializer
from core.models import Opcao

class OpcaoSerializer(ModelSerializer):
    
    class Meta:
        model = Opcao
        fields = '__all__'
        depth = 1