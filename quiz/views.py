
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz, Hello
from .serializers import QuizSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
import random

class HelloViewSet(viewsets.ViewSet):
    queryset = Hello.objects.all()
    def list(self, request):
        return Response("hello world!")

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    # 랜덤의 개수를 받기 위해 decorator를 사용하여 get method 수정
    @action(detail=True, methods=['GET'])
    #pk값을 받아 해당 개수만큼 quiz를 뽑아냄
    def random(self, request, pk=None):
        queryset = super().get_queryset()
        randomQuiz = random.sample(list(queryset), int(pk))
        serializer = QuizSerializer(randomQuiz, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)