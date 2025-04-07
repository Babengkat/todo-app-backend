from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from . import views
from django.urls import path, include


router = DefaultRouter()
router.register(r'', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]