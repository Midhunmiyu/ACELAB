from django.shortcuts import render, redirect

from home.forms import patientlogin
from home.models import patient


def patientdashboard(request):
    return render(request, 'patient/patientbase.html')



