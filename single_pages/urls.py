from django.urls import path
from . import views

app_name='single_pages'
urlpatterns = [
    path('', views.all_contents, name='all_contents'), # 전체 뷰 
    path('delete/todo/<int:pk>/', views.TodoDelete.as_view(), name='delete_todo'), # 삭제
    path('delete/doing/<int:pk>/', views.DoingDelete.as_view(),  name='delete_doing'),
    path('delete/done/<int:pk>/', views.DoneDelete.as_view(), name='delete_done'),
    path('delete/collaboration/<int:pk>/', views.CollaborationDelete.as_view(), name='delete_collaboration'),
    path('create-thing/',views.TodoCreate.as_view(), name='thing-create'), # 등록
    path('create-doingthing/',views.DoingCreate.as_view(), name='doingthing-create'),
    path('create-donething/',views.DoneCreate.as_view(), name='donething-create'), 
    path('create-colabthing/',views.CollaborationCreate.as_view(), name='colabthing-create'),
    
]

    # path('', CombinedTaskList.as_view(), name='combined-tasks'),
    # path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    # path('create-task/',TaskCreate.as_view(), name='tasks-create'),
    # path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    # path('task-delete/<int:pk>/', DeleteView.as_view(),name = 'task-delete'),