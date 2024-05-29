from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Account

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'date_of_birth', 'gender')
        



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'username')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        
