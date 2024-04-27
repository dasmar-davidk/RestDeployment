from cProfile import Profile

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer:
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
    extra_kwargs = {'password': {'write_only': True}}
    class ProfileSerializer(serializers.ModelSerializer):
        user = UserSerializer()
        class Meta:
            model = Profile
            fields = ['user', 'bio', 'city']
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['password'] = make_password(user_data['password'])
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile