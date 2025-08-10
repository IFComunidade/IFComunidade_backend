from rest_framework.serializers import ModelSerializer
from core.representante import Representante

class RepresentanteSerializer(ModelSerializer):
    
    class Meta:
        model = Representante
        fields = '__all__'