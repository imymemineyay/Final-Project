from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import CommentForm
from django.http import HttpResponse
from rest_framework.views import APIView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
#  , 붙이는 거 중요함

class Dashboard(APIView):
    def get(self, request):
        return render(request, 'business_management/dashboard.html')

    def post(self, request):
        return render(request, 'business_management/dashboard.html')

############################################################################

class PostList(UserPassesTestMixin, ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 4

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("users:login")

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context



############################################################################

# class PostList(ListView):
#     model = Post
#     ordering = '-pk'
#     paginate_by = 4
    
#     def get_context_data(self, **kwargs):
#         context = super(PostList, self).get_context_data()
#         context['categories'] = Category.objects.all()
#         context['no_category_post_count'] = Post.objects.filter(category=None).count()
#         return context

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    
    return render(
        request,
        'business_management/post_list.html',
        {
            'post_list':Post.objects.filter(category=category),
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        }
    )
    
    
class PostDetail(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context
    

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category']
   
    
    def form_valid(self,form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate,self).form_valid(form)
        else:
            return redirect('users/login.html')
    

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category']
    
    template_name = 'business_management/post_update_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate,self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
        


class PostDelete(DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('business_management:business_management')
    
    
    

def comments_create(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('business_management:postdetail', pk= post.pk)
        return redirect('business_management:postdetail', pk= post.pk)
    return redirect('business_management:business_management')




class CommentUpdate(LoginRequiredMixin,UpdateView):
    model = Comment
    form_class = CommentForm
    
    def dispatch(self, request, *args, **kwargs) :
        comment = self.get_object()
        if request.user.is_authenticated and request.user == comment.author:
            return super(CommentUpdate, self).dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.get_object().post.id
        return context
    
    
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url() + '#comment-list')
    else:
        raise PermissionError('Comment 삭제 권한이 없습니다.')
  