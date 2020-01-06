from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]

        extra_kwargs = {'password': {'write_only': True}}

        def validate(self, data):
            pw = data.get('password')
            pw2 = data.pop('password2')

            if pw != pw2:
                raise serializers.ValidationError("Passwords must match")

            return data
