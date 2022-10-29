from rest_framework import mixins, parsers, viewsets
from rest_framework.viewsets import ModelViewSet
from media.models import Image, Document
from media.serializers import (
    ImageUploadSerializer,
    DocumentUploadSerializer,
    ImageSerializer,
)


class CreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class ImageUploadViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]



