from rest_framework import serializers
from django.contrib.auth.models import User
from PasswordApp.models import PassWordModel,OrganizationModel
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class PassWordSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=PassWordModel
        fields="__all__"

class OrganizationSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=OrganizationModel
        fields="__all__"






