from rest_framework.serializers import ModelSerializer
from core.postagem import Postagem

class PostagemSerializer(ModelSerializer):
    
    class Meta:
        model = Postagem
        fields = '__all__'    