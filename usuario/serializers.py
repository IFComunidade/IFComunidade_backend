from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from django.contrib.auth.password_validation import validate_password
from .models import Usuario

class UsuarioSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirmar_senha = serializers.CharField(write_only=True)
    class Meta:
        model = Usuario
        fields = ["id", "email", "nome", "password", "confirmar_senha", "cpf", "matricula", "curso", "sigla"]
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirmar_senha']:
            raise serializers.ValidationError({"password": "As senhas não coincidem"})
        
    def create(self, validated_data):
        validated_data.pop("confirmar_senha")
        user = Usuario.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            nome = validated_data.get('nome'),
            matricula = validated_data.get('matricula'),
            curso = validated_data.get('curso'),
            cpf = validated_data.get('cpf'),
            sigla = validated_data.get('sigla'),
        )

        return user