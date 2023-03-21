from django.contrib import admin


from home.models import Login, doctor, patient, department, DoctorNotification, PatientNotification, \
    Feedback, DocSchedule, Appointment

# Register your models here.
admin.site.register(Login)
admin.site.register(doctor)
admin.site.register(patient)
admin.site.register(department)
admin.site.register(DoctorNotification)
admin.site.register(PatientNotification)
admin.site.register(Feedback)
admin.site.register(DocSchedule)
admin.site.register(Appointment)

