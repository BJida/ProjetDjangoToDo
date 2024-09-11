from rest_framework import routers
from todo.views import TodoViewSet, TodoListViewSet

router = routers.DefaultRouter()
router.register('todo',TodoViewSet)
router.register('todo-lists', TodoListViewSet)