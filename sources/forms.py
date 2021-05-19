from django import forms
from django.forms import ModelForm
from .models import Source

class SourceModelForm(forms.ModelForm):
  class Meta:
    model = Source
    fields = (
        'source',
    )