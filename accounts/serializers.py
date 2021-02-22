from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key', 'user']

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        extra_kwargs = {'password': {'write_only': True}, 'email': {'write_only': True}}
        fields = [
            "pk",
            "email",
            "password",
            "is_active",
            "date_joined",
            "avatar",
        ]
