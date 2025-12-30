from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
import requests

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['GET'])
def get_quote(request):
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    return Response({
        "quote": data["content"],
        "author": data["author"]
    })

@api_view(['GET'])
def task_report(request):
    total = Task.objects.count()
    completed = Task.objects.filter(is_completed=True).count()
    pending = total - completed

    return Response({
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending
    })
