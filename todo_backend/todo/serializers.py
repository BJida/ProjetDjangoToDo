from rest_framework import serializers

from todo.models import Todo, TodoList

class TodoSerializer(serializers.ModelSerializer):

    dueDate = serializers.DateField(source='due_date')

    class Meta:
        model = Todo
        fields = ('id', 'title', 'dueDate')

class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = '__all__' 