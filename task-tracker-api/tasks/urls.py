from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, get_quote, task_report

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('quote/', get_quote),
    path('report/', task_report),
]
