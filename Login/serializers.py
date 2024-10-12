from django.contrib.auth.models import User
from .models import HeroListModel, Candidate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

#serializer for creating new user through restframework
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password','is_staff')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_staff=validated_data['is_staff'],
        )
        Token.objects.get_or_create(user=user)  # Token is created but not returned
        return user  # Return the user object

# 
class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroListModel
        fields = '__all__'


class CadidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        # fields = ['name', 'dob', 'skills', 'yearOfExp', 'qualification']
        fields = '__all__'
