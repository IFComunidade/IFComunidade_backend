from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField
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
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmar_senha = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ["id", "email", "nome", "password", "confirmar_senha", "cpf", "matricula", "curso", "sigla", "tipo", "foto", "foto_attachment_key"]
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirmar_senha']:
            raise serializers.ValidationError({"password": "As senhas não coincidem"})
        return attrs
        
    def create(self, validated_data):
        validated_data.pop("confirmar_senha")
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