from django.db import models
from categories.models import Category
from sources.models import Source
from users.models import User
from django.shortcuts import reverse

# Create your models here.


class Lead(models.Model):
    
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='NEW')
    task = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, default='misen', on_delete=models.CASCADE)
    deposit = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name




class Comment(models.Model):
    lead = models.ForeignKey(Lead, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.lead, self.user)