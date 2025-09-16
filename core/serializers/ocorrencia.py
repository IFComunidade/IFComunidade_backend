from rest_framework.serializers import ModelSerializer, SlugRelatedField, SerializerMethodField
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Ocorrencia

class OcorrenciaSerializer(ModelSerializer):
    imagem_attachment_key = SlugRelatedField(
        source='imagem',
        queryset = Image.objects.all(),
        slug_field = 'attachment_key',
        required = False,
        write_only = True,
    )
    imagem = ImageSerializer(required=False, read_only=True)

    tipo = SerializerMethodField()
    class Meta:
        model = Ocorrencia
        fields = '__all__'
        depth = 1

    def get_tipo(self, obj):
        return obj.get_tipo_display()