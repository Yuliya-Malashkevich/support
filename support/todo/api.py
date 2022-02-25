from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()  # наши объекты в бд
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer   # указали класс сериалайзера

 #далее создаём файл urls.py в папке todo