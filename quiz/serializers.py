from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'body', 'answer', ]
