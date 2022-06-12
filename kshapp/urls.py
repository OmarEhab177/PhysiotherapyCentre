from django.urls import path 
from . import views


app_name = 'kshapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('sections', views.section, name='section'),
    path('new-patient', views.new_patient, name='new-patient'),
    path('new-patient-type', views.new_patient_type, name='new-patient-type'),
    path('disability', views.new_disability, name='new-disability'),
    path('patients', views.patients, name='patients'),
    path('therapist', views.therapist, name='therapist'),
    path('appointment', views.appointment, name='appointment'),
    path('therapistprofile.html', views.therapistprofile, name='therapistprofile'),
    path('login.html',views.loginpage, name='login'),
    path('logout.html',views.logoutuser, name='logout'),

   
]
