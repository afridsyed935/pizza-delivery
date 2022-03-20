from rest_framework import serializers
from .models import User


class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=25)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields  = ['username', 'email', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail=("Username already exists"))
            
        email_exists = User.objects.filter(username=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail=("Email already exists"))
            
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user