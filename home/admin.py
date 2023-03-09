from django.contrib import admin

from home import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.doctor)
admin.site.register(models.patient)
admin.site.register(models.department)
admin.site.register(models.DoctorNotification)
admin.site.register(models.PatientNotification)
admin.site.register(models.Feedback)