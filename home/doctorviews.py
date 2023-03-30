from django.shortcuts import render, redirect

from home.forms import doctorlogin
from home.models import doctor, Feedback, Appointment, patient, DoctorNotification


def doctordashboard(request):
    total=DoctorNotification.objects.all().count()
    return render(request, 'doctor/doctorbase.html',{'total':total})


def doc_view_feedback(request):
    data = Feedback.objects.all()
    return render(request, 'doctor/doc_view_feedback.html', {'data': data})


def doc_view_appointments(request):
    doc= doctor.objects.get(user=request.user)
    data = Appointment.objects.filter(Schedule__Doc_name=doc)

    return render(request,'doctor/doc_view_appointments.html',{'data':data})


def doc_view_patients(request):
    data=patient.objects.all()
    return render(request,'doctor/doc_view_patients.html',{'data':data})


def doc_view_notificaction(request):
    data=DoctorNotification.objects.all()
    return render(request,'doctor/doc_view_notification.html',{'data':data})