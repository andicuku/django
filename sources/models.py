from django.db import models

# Create your models here.

class Source (models.Model):
   
    source = models.CharField(unique=True, max_length=30)
    
    def __str__(self):
        return self.source

