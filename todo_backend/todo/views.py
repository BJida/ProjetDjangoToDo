from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo, TodoList
from todo.serializers import TodoSerializer, TodoListSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes=(IsAuthenticated,) #pour securiser le code
    filterset_fields = ['due_date', 'favourite', 'completed']
    search_fields =['title']

class TodoListViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes=(IsAuthenticated,)