from django.shortcuts import render, redirect

from home.forms import doctorlogin
from home.models import doctor


def doctordashboard(request):
    return render(request,'doctor/doctorbase.html')

