from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Prompt
from .serializers import PromptSerializer
from django.contrib.auth.models import User
from urllib.parse import unquote



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



@api_view(['GET'])
def get_prompts_by_wikipedia_link(request):
    wikipedia_link = request.query_params.get('wikipedia_link', None)
    if wikipedia_link is not None:
        wikipedia_link = wikipedia_link.strip()  # Remove leading/trailing whitespace
        wikipedia_link = unquote(wikipedia_link)  # Decode URL-encoded characters
        prompts = Prompt.objects.filter(Wikipedia_link=wikipedia_link)
        if not prompts:
            return Response({"error": "No prompts found for the given Wikipedia_link"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error": "Wikipedia_link parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
