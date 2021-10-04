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

  
class LeadModifyForm(forms.Form):
  user = forms.ModelChoiceField(queryset= User.objects.none())
  category = forms.ModelChoiceField(queryset=Category.objects.none())

  def __init__(self, *args, **kwargs):
    users = User.objects.all()
    categories = Category.objects.all()
    super(LeadModifyForm, self).__init__(*args, **kwargs)
    self.fields["user"].queryset = users
    self.fields["category"].queryset = categories


