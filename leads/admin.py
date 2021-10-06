from django.contrib import admin
from .models import Comment, Lead

# Register your models here.

admin.site.register(Lead)
admin.site.register(Comment)