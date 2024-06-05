from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id', 'Prompt_title', 'Prompt', 'Wikipedia_link', 'Code', 'Summary', 'User', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
