from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length = 120)

    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create(**validated_data)




