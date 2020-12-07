from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import CustomUser


# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'first_name', 'last_name', 'is_active',
            'last_login', 'is_superuser', 'password'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        return user
