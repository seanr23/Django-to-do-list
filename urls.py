# tasks/urls.py
from django.urls import path
from tasks import views
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Ensure this matches the view name
    path('update_task/<str:pk>/', views.update_task, name='update_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task')
]
