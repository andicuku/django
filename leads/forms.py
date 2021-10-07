from django.db.models.fields import DateTimeField
from .models import Comment, Lead, User, Category
from django import forms
from django.forms import Textarea
from flatpickr import DateTimePickerInput


class LeadModelForm(forms.ModelForm):
  class Meta:
    model = Lead
    fields = (
        'name',
        'phone',
        'email',
        'source',
        'category',
        'task',
        'user',
        'deposit'
    )
    widgets = {
        'task': DateTimePickerInput(attrs={'placeholder':'Select Date/Time.'}),
    }

  
class LeadModifyForm(forms.ModelForm):
  class Meta:
    model = Lead
    fields = (
      'user',
      'category'
    )

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('body',)

    widgets = {
      'body': Textarea(attrs={'cols': 14, 'rows': 2}),
    }