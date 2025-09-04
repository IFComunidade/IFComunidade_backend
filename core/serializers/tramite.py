from rest_framework.serializers import ModelSerializer
from core.models import Tramite

class TramiteSerializer(ModelSerializer):
    class Meta:
        model = Tramite
        fields = '__all__'