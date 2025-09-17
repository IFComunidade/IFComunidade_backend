from rest_framework import serializers
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Ocorrencia

class OcorrenciaSerializer(serializers.ModelSerializer):
    imagem_attachment_key = serializers.SlugRelatedField(
        source='imagem',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        allow_null=True,
        required=False,
        write_only=True,
    )

    imagem = ImageSerializer(required=False, read_only=True)
    
    categoria = serializers.PrimaryKeyRelatedField(
        queryset=Ocorrencia._meta.get_field('categoria').related_model.objects.all(),
        write_only=True
    )
    categoria_display = serializers.SerializerMethodField(read_only=True)
    status_display = serializers.SerializerMethodField(read_only=True)
    tipo_display = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ocorrencia
        fields = '__all__'

    def get_categoria_display(self, obj):
        return str(obj.categoria) 

    def get_tipo_display(self, obj):
        return obj.get_tipo_display()
    
    def get_status_display(self, obj):
        return obj.get_status_display()
