from .models import Lead, User, Category
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
        'comment',
    )

    widgets = {
        'comment': Textarea(attrs={'cols': 20, 'rows': 4}),
        'task': DateTimePickerInput(attrs={'placeholder':'Select Date/Time.'}),
    }

  
class LeadModifyForm(forms.ModelForm):
  class Meta:
    model = Lead
    fields = (
      'user',
      'category'
    )