from django.urls import path
from . import views

app_name = "business_management"

urlpatterns = [
    path('', views.PostList.as_view(), name="business_management"),
    path('<int:pk>/', views.PostDetail.as_view(), name="postdetail"),
    path('category/<str:slug>/', views.category_page, name= "category"),
    path('create_post/', views.PostCreate.as_view(), name = "postcreate"),
    path('update_post/<int:pk>/', views.PostUpdate.as_view(), name="postupdate"),
    path('<int:pk>/new_comment/', views.comments_create, name= "comment"),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard_page"),
    path('delete_post/<int:pk>/',views.PostDelete.as_view(), name="postdelete"),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view(), name = 'commentupdate'),
    path('delete_comment/<int:pk>/',views.delete_comment, name="commentdelete"),
]

