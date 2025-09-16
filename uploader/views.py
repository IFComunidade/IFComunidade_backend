from rest_framework import mixins, parsers, viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from uploader.models import Document, Image
from uploader.serializers import DocumentUploadSerializer, ImageUploadSerializer


class CreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


@extend_schema(tags=["Uploader - Documento"])
class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all() #  pylint: disable=no-member
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

@extend_schema(tags=["Uploader - Imagem"])
class ImageUploadViewSet(CreateViewSet):
    permission_classes = [AllowAny]
    queryset = Image.objects.all() #  pylint: disable=no-member
    serializer_class = ImageUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
