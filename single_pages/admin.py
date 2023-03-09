from django.contrib import admin

from .models import Todo, Doing, Done, Collaboration

# Register your models here. admin 페이지에 Task 등록
# admin.site.register(Todo)
admin.site.register(Todo)
admin.site.register(Doing)
admin.site.register(Done)
admin.site.register(Collaboration)