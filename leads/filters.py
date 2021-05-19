from .models import Lead
import django_filters
from flatpickr import DateTimePickerInput



class LeadFilter(django_filters.FilterSet):

    class Meta:
        model = Lead
        fields = {
         'name': ['icontains', ],
         'phone': ['icontains', ],
         'source':['exact',] ,
         'created_at': ['date', 'date__gt', 'date__lt',],
         'category': ['exact', ],
         'user': ['exact', ],
        }


    widgets = {
         'created_at__date': DateTimePickerInput(attrs={'placeholder':'Select Date/Time.'}),
         'created_at__date__gt': DateTimePickerInput(attrs={'placeholder':'Select Date/Time.'}),
         'created_at__date__lt': DateTimePickerInput(attrs={'placeholder':'Select Date/Time.'}),
      }