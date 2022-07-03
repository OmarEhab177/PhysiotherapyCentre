from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'kshapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('section', views.section, name='section'),
    path('patients', views.patients, name='patients'),
    path('patients/patient/<int:pk>', views.view_patient, name='view-patient'),
    path('new-patient', views.new_patient, name='new-patient'),
    path('delete-patient', views.delete_patient, name='delete-patient'),
    path('edit-patient', views.edit_patient, name='edit-patient'),
    path('new-patient-type', views.new_patient_type, name='new-patient-type'),
    path('disability', views.new_disability, name='new-disability'),
    path('new-appointment', views.new_appointment, name='new-appointment'),
    path('appointments', views.appointments, name='appointments'),
    path('appointment/<int:pk>', views.appointment_detail, name='appointment-detail'),
    path('edit-appoint', views.edit_appoint, name='edit-appoint'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
