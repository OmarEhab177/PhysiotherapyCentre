import django_filters
from .models import *
from django_filters import DateFilter
from django.utils.translation import gettext_lazy as _
from django.forms import Widget
from django.forms import ModelForm


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date",lookup_expr='gte',label='From Date ')
    end_date = DateFilter(field_name="date",lookup_expr='lte',label='To Date ')
    class Meta:
        model = Appointment
        fields = [
                
                'time',
                'patient',
                'service',
                'status',
                'action',
                'therapist',
             ] 
        labels = {
            'patient': _('التاريخ'),

        
        }
