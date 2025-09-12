from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .models import Usuario
from uploader.models import Image
from uploader.serializers import ImageSerializer

class UsuarioSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required = False,
        allow_null = True,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = Usuario
        fields = ["id", "email", "nome", "password", "cpf", "matricula", "curso", "sigla", "tipo", "foto", "foto_attachment_key"]
        
    def create(self, validated_data):
        user = Usuario.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            foto = validated_data.get('foto'),
            nome = validated_data.get('nome'),
            matricula = validated_data.get('matricula'),
            curso = validated_data.get('curso'),
            tipo = validated_data.get('tipo'),
            cpf = validated_data.get('cpf'),
            sigla = validated_data.get('sigla'),
        )

        return user
    
## CUSTOMIZANDO SERIALIZER PARA TOKEN

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UsuarioSerializer(self.user).data
        return data