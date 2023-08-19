from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "username", "phone_number"]

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            # phone_number=validated_data['phone_number']
            )

        user.set_password(validated_data['password'])
        user.save()
        return user
