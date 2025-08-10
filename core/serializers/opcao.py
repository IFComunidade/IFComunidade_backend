from rest_framework.serializers import ModelSerializer
from core.opcao import Opcao

class OpcaoSerializer(ModelSerializer):
    
    class Meta:
        model = Opcao
        fields = '__all__'