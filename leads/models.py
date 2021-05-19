from django.db import models
from categories.models import Category
from sources.models import Source
from users.models import User

# Create your models here.


class Lead(models.Model):
    
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='NEW')
    task = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, default='misen', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

