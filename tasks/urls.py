from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('task/<str:slug>', views.task_detail, name='task-detail'),
    path('task/<str:slug>/toggle/', views.task_toggle, name='task-toggle'),
    path('task/<str:slug>/edit/', views.task_edit, name='task-edit'),
    path('task/<str:slug>/delete/', views.task_delete, name='task-delete'),
    path('add/', views.add_task, name='add-task'),
    path('done/', views.show_done, name='show-done'),
    path('pending/', views.show_pending, name='show-pending'),
]
