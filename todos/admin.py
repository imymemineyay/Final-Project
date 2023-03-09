from django.contrib import admin
# from .models import Todo
from .models import Task, Long_Term_Task

# Register your models here. admin 페이지에 Task 등록
# admin.site.register(Todo)
admin.site.register(Task)
admin.site.register(Long_Term_Task)