from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # This will create routes for CRUD operations

urlpatterns = [
    path('api/', include(router.urls)),  # API base URL: /api/tasks/
]
