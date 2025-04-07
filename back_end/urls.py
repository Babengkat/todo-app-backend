from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks', include('todo_app.urls')),
    path('api/', include('todo_app.urls')),
    path('', include('todo_app.urls')),  # ← this is important
]
