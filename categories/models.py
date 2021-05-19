from django.db import models

# Create your models here.

class Category (models.Model):
   
    category = models.CharField(unique=True, max_length=30)
    
    def __str__(self):
        return self.category

