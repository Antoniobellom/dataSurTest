from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Usuario, UnidadEjercito
from django.contrib.auth.password_validation import validate_password

class UsuarioSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Usuario
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password', 'telefono')
        extra_kwargs = {
            'username': {'required': True},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            telefono=validated_data.get('telefono', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class EjercitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadEjercito
        fields = ['id', 'nombre', 'fuerza', 'movimiento', 'costo']