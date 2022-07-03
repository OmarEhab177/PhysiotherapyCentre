from django.contrib import admin
from .models import *


# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ['date', 'time', 'patient', 'note', 'status']
#     list_editable = ['status']
#     list_filter = ['date', 'patient']


admin.site.register(PatientType)
admin.site.register(Patient)
admin.site.register(Section)
admin.site.register(Therapist)
# admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Appointment)
admin.site.register(Disability)
