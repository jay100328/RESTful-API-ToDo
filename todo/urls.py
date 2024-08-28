from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy
from todo.views import get_todo

urlpatterns = [
    # path('post_todo/', post_todo),
    path('get_todo/', get_todo),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
]
