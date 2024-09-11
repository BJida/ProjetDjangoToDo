from datetime import datetime
from django.test import TestCase

from todo.models import Todo, TodoList

class TodoTestCase(TestCase):
    DUMMY_TODO_TITLE ='Test Element'
    def setUp(self):
        self.todoList = TodoList()
        self.todoList.name ='Test Todo List'
        self.todoList.save()

        self.todoListTestTestElement = Todo()
        self.todoListTestTestElement.title = self.DUMMY_TODO_TITLE
        self.todoListTestTestElement.due_date = datetime.today()
        self.todoListTestTestElement.completed =True
        self.todoListTestTestElement.favourite = False
        self.todoListTestTestElement.list =self.todoList
        self.todoListTestTestElement.save()

    def test_create_todo(self):
        nbr_of_todo_before_add=Todo.objects.count()

        new_todo = Todo()
        new_todo.title="Acheter de l'eau"
        new_todo.due_date = datetime.today()
        new_todo.favourite = True
        new_todo.completed = False
        new_todo.list = self.todoList
        new_todo.save()

        nbr_of_todo_after_add =Todo.objects.count()

        self.assertTrue(nbr_of_todo_after_add== nbr_of_todo_before_add+1)
    

    def test_update_todo(self):

        self.assertEqual(self.todoListTestTestElement.title, self.DUMMY_TODO_TITLE)

        self.todoListTestTestElement.title= 'Changed'
        self.todoListTestTestElement.save()

        tempElement = Todo.objects.get(pk=self.todoListTestTestElement.pk)

        self.assertEqual(tempElement.title, 'Changed')
    
    def test_delete_todo(self):
        nbr_of_todo_before_delete = Todo.objects.count()

        self.todoListTestTestElement.delete()

        nbr_of_todo_after_delete =Todo.objects.count()

        self.assertTrue(nbr_of_todo_after_delete==nbr_of_todo_before_delete-1)
