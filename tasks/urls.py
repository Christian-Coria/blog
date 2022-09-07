from django.urls import path
from tasks.views import delete_task, create_task, list_tasks

urlpatterns = [
  path('list_tasks', list_tasks , name='list_tasks'),
  path('new/', create_task, name='create_task'),
  path('delete_task/<int:task_id>/', delete_task, name='delete_task'),


]