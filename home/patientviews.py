from django.shortcuts import render, redirect

from home.forms import patientlogin
from home.models import patient, department, doctor


def patientdashboard(request):
    return render(request, 'patient/patientbase.html')


def patient_view_department(request):
    data = department.objects.all()
    return render(request, 'patient/view_departments.html', {'data': data})


def pattient_view_doctor(request):
    data = doctor.objects.all()
    return render(request, 'patient/view_doctors.html', {'data': data})
