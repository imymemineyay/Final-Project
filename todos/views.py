from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
# from .models import Todo
from .models import Task, Long_Term_Task
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin




class CombinedTaskList(UserPassesTestMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("users:login")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['long_term_tasks'] = Long_Term_Task.objects.all()
        return context

# 로그인 해야 페이지가 보여지게 만들어야 함

# class CombinedTaskList(ListView):
#     model = Task
#     context_object_name = "tasks"
    
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['long_term_tasks'] = Long_Term_Task.objects.all()
#         return context


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todos:combined-tasks')
    
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todos:combined-tasks')


class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todos:combined-tasks')
    

##########################################################

class Long_Term_TaskDetail(DetailView):
    model = Long_Term_Task
    context_object_name = "long_term_task"
    
    
class Long_Term_TaskCreate(CreateView):
    model = Long_Term_Task
    fields = '__all__'
    success_url = reverse_lazy('todos:combined-tasks')
    
    
class Long_Term_TaskUpdate(UpdateView):
    model = Long_Term_Task
    fields = '__all__'
    success_url = reverse_lazy('todos:combined-tasks')


class Long_Term_DeleteView(DeleteView):
    model = Long_Term_Task
    context_object_name = 'long_term_task'
    success_url = reverse_lazy('todos:combined-tasks')
    
    
    

# Task 의 ListView

# class TaskList(ListView):
#     model = Task
#     context_object_name = "tasks"


# Long_Term_TaskList 의 ListView 
  
# class Long_Term_TaskList(ListView):
#    model = Long_Term_Task
#    context_object_name = "long_term_tasks"
#    template_name = "todos/tasks_list.html"


