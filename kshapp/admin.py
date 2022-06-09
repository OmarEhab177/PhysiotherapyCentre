from django.contrib import admin
from .models import *


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'therapist_name', 'patient_name', 'note', 'status']
    list_editable = ['status']
    list_filter = ['date', 'patient_name']
    search_fields = ['therapist_name']


admin.site.register(PatientType)
admin.site.register(Patient)
admin.site.register(Section)
admin.site.register(Therapist)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Disability)
