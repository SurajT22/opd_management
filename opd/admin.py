from django.contrib import admin
from opd.models import Patient, Doctor, Appointment, Prescription, Billing

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Billing)
