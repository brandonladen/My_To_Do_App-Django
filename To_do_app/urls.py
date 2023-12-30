from django.urls import path
from .views import view_task, create_task, delete_task, edit_task

urlpatterns = [
    path('', view_task, name='home'),
    path('create/', create_task, name='create'),
    path('<int:task_id>/', delete_task, name='delete'),
    path('edit/<int:taskid>/', edit_task, name='edit'),
]