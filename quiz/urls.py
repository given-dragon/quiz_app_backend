from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloViewSet, QuizViewSet

router = DefaultRouter()
router.register('hello', HelloViewSet)
router.register('data', QuizViewSet)
urlpatterns = [
    path('', include(router.urls)),    
]
