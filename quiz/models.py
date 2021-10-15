from django.db import models

# Create your models here.

# 걍 출력해보려고 만든 모델(굳이 모델로 할 필요 없음..)
class Hello(models.Model):
    pass

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()