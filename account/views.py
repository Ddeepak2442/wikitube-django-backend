from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import SignUpSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register(request):
    data = request.data
    user_serializer = SignUpSerializer(data=data)

    if user_serializer.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user_serializer.save()
            return Response({'message': 'User registered.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request):
    user = UserSerializer(request.user)
    return Response(user.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request):
    user = request.user
    data = request.data

    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.username = data.get('email', user.username)
    user.email = data.get('email', user.email)

    if data.get('password'):
        user.password = make_password(data['password'])

    user.save()

    user_profile = user.userprofile
    user_profile.date_of_birth = data.get('date_of_birth', user_profile.date_of_birth)
    user_profile.gender = data.get('gender', user_profile.gender)
    user_profile.save()

    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)
