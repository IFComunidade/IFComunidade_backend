from rest_framework.serializers import ModelSerializer
from core.models import Postagem

class PostagemSerializer(ModelSerializer):
    
    class Meta:
        model = Postagem
        fields = '__all__'    