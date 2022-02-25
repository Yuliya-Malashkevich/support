from rest_framework import serializers
from .models import Todo

#сериализуем все поля модели  в json формат
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__al__'
#далее создаем новый файл api.py
