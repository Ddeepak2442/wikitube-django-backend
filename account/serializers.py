from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(required=True)
    gender = serializers.ChoiceField(choices=UserProfile.GENDER_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'date_of_birth', 'gender')
        extra_kwargs = {
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False},
            'password': {'required': True, 'allow_blank': False, 'min_length': 6},
        }

    def create(self, validated_data):
        date_of_birth = validated_data.pop('date_of_birth')
        gender = validated_data.pop('gender')
        email = validated_data['email']
        user = User.objects.create_user(
            username=email,
            email=email,
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        UserProfile.objects.create(user=user, date_of_birth=date_of_birth, gender=gender)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('date_of_birth', 'gender')

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',  'userprofile')
 