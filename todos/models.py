from django.db import models
from users.models import *

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null =True, blank = True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateField(auto_now_add= True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['create'] # 오름차순 
        

class Long_Term_Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null =True, blank = True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateField(auto_now_add= True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['create'] # 오름차순     
        
    