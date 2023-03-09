from django.db import models
import os 
from users.models import *




# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=200, unique= True, allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/business_management/category/{self.slug}/'
    

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    
    head_image = models.ImageField(upload_to='business_management/images/%Y/%m/%d/', blank = True)
    file_upload = models.FileField(upload_to='business_management/files/%Y/%m/%d/', blank = True)
    
    created_at = models.DateTimeField(auto_now_add = True) 
    updated_at = models.DateTimeField(auto_now = True) # 게시물 업데이트 후 시간 변경 표시 
    author = models.ForeignKey(User, null=True,on_delete = models.SET_NULL)
    
    category = models.ForeignKey(Category, null = True, on_delete=models.SET_NULL)
       
    
    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'
    
    
    def get_absolute_url(self):
        return f'/business_management/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.author}::{self.content}'
    
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
   


    

    