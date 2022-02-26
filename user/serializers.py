from dataclasses import fields
from pyexpat import model
from user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "first_name": {"required": False, "allow_null": False},
            "last_name": {"required": False, "allow_null": False},
            "company_name": {"required": False, "allow_null": False},
            "city": {"required": False, "allow_null": False},
            "state": {"required": False, "allow_null": False},
            "zip": {"required": False, "allow_null": False},
            "email": {"required": False, "allow_null": False},
            "web": {"required": False, "allow_null": False},
            "age": {"required": False, "allow_null": False},
        }
