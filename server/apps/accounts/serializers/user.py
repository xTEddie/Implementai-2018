from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active')


class UserSerializerLogin(UserSerializer):

    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active', 'token')

    def get_token(self, user):
        """
            Get or create token
        """

        token, created = Token.objects.get_or_create(user=user)
        return token.key
