# flashcard/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Prompt
from .serializers import PromptSerializer
from django.contrib.auth.models import User



@api_view(['POST'])
def create_prompt(request):
    if request.method == 'POST':
        data = request.data

        # Retrieve the user based on the provided email
        user_email = data.get('User')
        if user_email:
            try:
                user = User.objects.get(email=user_email)
            except User.DoesNotExist:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Associate the prompt with the retrieved user
        data['User'] = user.pk

        serializer = PromptSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Prompt created successfully.'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

