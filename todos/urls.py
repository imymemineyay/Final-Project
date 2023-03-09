from django.urls import path
from .views import  TaskDetail, TaskCreate, TaskUpdate, DeleteView
from .views import  Long_Term_TaskDetail, Long_Term_TaskCreate, Long_Term_TaskUpdate, Long_Term_DeleteView, CombinedTaskList

app_name='todos'
urlpatterns = [
    path('', CombinedTaskList.as_view(), name='combined-tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/',TaskCreate.as_view(), name='tasks-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(),name = 'task-delete'),
    
    path('long-term-task/<int:pk>/',  Long_Term_TaskDetail.as_view(), name='long-term-task'),
    path('create-long-term-task', Long_Term_TaskCreate.as_view(), name='long-term-tasks-create'),
    path('long-term-task-update/<int:pk>/', Long_Term_TaskUpdate.as_view(), name='long-term-task-update'),
    path('long-term-task-delete/<int:pk>/', Long_Term_DeleteView.as_view(),name = 'long-term-task-delete'),
    
    #  <!-- 원본 -->
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:todo_id>/delete', views.delete, name='delete'),
    # path('<int:todo_id>/update', views.update, name='update'),
    # path('add/', views.add, name='add') TaskList, Long_Term_TaskList,
    # path('',TaskList.as_view(), name='tasks'),
    # path('', Long_Term_TaskList.as_view(), name='long-term-tasks'),
]