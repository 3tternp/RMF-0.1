from rest_framework import serializers
from .models import User, Risk

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
