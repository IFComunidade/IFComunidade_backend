from rest_framework import serializers
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Ocorrencia, Categoria

class OcorrenciaSerializer(serializers.ModelSerializer):
    imagem_attachment_key = serializers.SlugRelatedField(
        source='imagem',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    
    categoria = serializers.SlugRelatedField(
    queryset=Categoria.objects.all(),
    slug_field='id',  
    )

    imagem = ImageSerializer(required=False, read_only=True)

    tipo = serializers.IntegerField(write_only=True)
    tipo_display = serializers.SerializerMethodField(read_only=True)

    
    
    class Meta:
        model = Ocorrencia
        fields = '__all__'
        # depth = 1

    def get_tipo_display(self, obj):
        return obj.get_tipo_display()
