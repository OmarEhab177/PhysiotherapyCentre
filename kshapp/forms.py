from django import forms 
from .models import *


class teacherform(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = '__all__'
  

class newform(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
class PatientTypeForm(forms.ModelForm):
    class Meta:
        model = PatientType
        fields = '__all__'
        
        widget = {
            'patient_type': forms.TextInput(attrs={'class': 'form-control'}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DisabilityForm(forms.ModelForm):
    class Meta:
        model = Disability
        fields = '__all__'
        
        widget = {
            'dis_type': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


class AppointForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
