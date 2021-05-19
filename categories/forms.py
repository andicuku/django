from django import forms
from django.forms import ModelForm
from .models import Category

class CategoryModelForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = (
        'category',
    )