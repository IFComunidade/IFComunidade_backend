from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer
from core.models import Postagem
from usuario.serializers import UsuarioSerializer

class PostagemSerializer(ModelSerializer):
    imagem_attachment_key = SlugRelatedField(
        source='imagem',
        queryset = Image.objects.all(),
        slug_field = 'attachment_key',
        required = False,
        write_only = True,
    )
    usuario = UsuarioSerializer(read_only=True)
    imagem = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Postagem
        fields = '__all__'   