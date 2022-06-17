from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'kshapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('section', views.section, name='section'),
    path('new-patient', views.new_patient, name='new-patient'),
    # path('edit-patient', views.edit_patient, name='edit-patient'),
    path('new-patient-type', views.new_patient_type, name='new-patient-type'),
    path('disability', views.new_disability, name='new-disability'),
    path('patients', views.patients, name='patients'),
    path('therapist', views.therapist, name='therapist'),
    path('appointment', views.appointment, name='appointment'),
    path('therapistprofile', views.therapistprofile, name='therapistprofile'),
    path('login',views.loginpage, name='login'),
    path('logout',views.logoutuser, name='logout'),

   
]
