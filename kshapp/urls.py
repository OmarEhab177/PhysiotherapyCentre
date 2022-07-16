from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'kshapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('sections', views.sections, name='sections'),
    path('new-section', views.new_section, name='new-section'),
    path('section-detail/<int:pk>', views.SectionView.as_view(), name='section-detail'),
    path('edit-section', views.edit_section, name='edit-section'),
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
    path('therapists', views.therapists, name='therapists'),
    path('therapist-detail/<int:pk>', views.TherapistView.as_view(), name='therapist-detail'),
    path('edit-therapist', views.edit_therapist, name='edit-therapist'),
    path('new-therapist', views.new_therapist, name='new-therapist'),
    path('therapist-appointmets', views.therapist_appointments, name='therapist-appointmets'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
