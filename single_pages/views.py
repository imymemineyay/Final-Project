from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo, Doing, Done, Collaboration
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.contrib import messages



def all_contents(request):
    if request.user.is_authenticated:
        # Query all 4 models and their objects
        todo_list = Todo.objects.filter(user=request.user)
        doing_list = Doing.objects.filter(user=request.user)
        done_list = Done.objects.filter(user=request.user)
        collaboration_list = Collaboration.objects.filter(user=request.user)

        # Combine all the objects into a single list
        contents_list = list(todo_list) + list(doing_list) + list(done_list) + list(collaboration_list)

        # Sort the list by the 'create' field of each object
        contents_list.sort(key=lambda x: x.create)

        # Define context data for each queryset
        context_data = {
            'things': todo_list,
            'doingthings': doing_list,
            'donethings': done_list,
            'collaborationthings': collaboration_list,
            'contentsthings': contents_list
        }

        # Create a list of dictionaries with each object's details
        content_dicts = []
        for thing in contents_list:
            content_dict = {
                'id': thing.pk,
                'title': thing.title,
                'description': thing.description,
                'complete': thing.complete,
                'create': thing.create,
            }

        # Render the template with the combined list of objects and the context data
        return render(request, 'single_pages/all_contents.html', context_data)
    
    return redirect('users:login')


### Todo ###

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "thing"
    
    
class TodoCreate(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'single_pages/todo_form.html'
    success_url = reverse_lazy('single_pages:all_contents')
    
    
class TodoUpdate(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('single_pages:all_contents')


class TodoDelete(DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('single_pages:all_contents')



 ### Doing ###
    
    
class DoingDetail(DetailView):
    model = Doing
    context_object_name = "doingthing"
    
    
class DoingCreate(CreateView):
    model = Doing
    template_name = 'single_pages/doing_form.html'
    fields = '__all__'
    success_url = reverse_lazy('single_pages:all_contents')
    
    
class DoingUpdate(UpdateView):
    model = Doing
    fields = '__all__'
    success_url = reverse_lazy('single_pages:all_contents')
    
class DoingDelete(DeleteView):
    model = Doing
    context_object_name = 'dos'
    success_url = reverse_lazy('single_pages:all_contents')
    
    
###  Done  ###  
    
class DoneDetail(DetailView):
    model = Done
    context_object_name = "donething"
    
    
class DoneCreate(CreateView):
    model = Done
    fields = '__all__'
    template_name = 'single_pages/done_form.html'
    success_url = reverse_lazy('single_pages:all_contents')
    
    
class DoneUpdate(UpdateView):
    model = Done
    fields = '__all__'
    success_url = reverse_lazy('single_pages:all_contents')
    
class DoneDelete(DeleteView):
    model = Done
    context_object_name = 'pp'
    success_url = reverse_lazy('single_pages:all_contents')
    
    
    
###  Collaboration  ###
    
class CollaborationDetail(DetailView):
    model = Collaboration
    context_object_name = "colabthing"
    
    
class CollaborationCreate(CreateView):
    model = Collaboration
    fields = '__all__'
    template_name = 'single_pages/colab_form.html'
    success_url = reverse_lazy('single_pages:all_contents')
    
    
class CollaborationUpdate(UpdateView):
    model = Collaboration
    fields = '__all__'
    success_url = reverse_lazy('single_pages:all_contents')
    
class CollaborationDelete(DeleteView):
    model = Collaboration
    context_object_name = 'col'
    success_url = reverse_lazy('single_pages:all_contents')





