from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser


#User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'first_name', 'last_name', 'is_active', 
            'last_login', 'is_superuser', 'password'
            )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'], validated_data['password']
            )

        return user
            
            
#Register
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = 'id', 'username', 'password'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'], validated_data['password']
            )

        return user