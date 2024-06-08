from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id', 'Prompt_title', 'Prompt', 'Wikipedia_link', 'Code', 'Summary', 'User','created_at']
        read_only_fields = ['id', 'created_at']


# class PromptLimitedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Prompt
#         fields = ['Prompt_title', 'Prompt', 'Code', 'Summary']
