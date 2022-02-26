from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

@csrf_exempt
def todoApi(request, id=0):
    if request.method=='GET':
        todos = Todo.objects.all()
        todo_serializer=TodoSerializer(todos,many=True)
        return JsonResponse(todo_serializer.data,safe=False)
    elif request.method=='POST':
        todo_data=JSONParser().parse(request)
        todo_serializer=TodoSerializer(data=todo_data)
        if todo_serializer. is_valid():
            todo_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        todo_data=JSONParser().parse(request)
        todo=Todo.objects.get(TodoId=todo_data['TodoId'])
        todo_serializer=TodoSerializer(todo,data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        todo=Todo.objects.get(TodoId=id)
        todo.delete()
        return JsonResponse("Deleted Successfully",safe=False)
