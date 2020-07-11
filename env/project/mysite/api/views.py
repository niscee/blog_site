from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializers
from .models import Task

@api_view(['GET'])
def index(request):
    api_urls = {
        'List': '/task-list/',
        'Detail-view': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskdetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializers(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskcreate(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
       serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskupdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializers(data=request.data, instance=tasks)
    if serializer.is_valid():
       serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskdelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)




