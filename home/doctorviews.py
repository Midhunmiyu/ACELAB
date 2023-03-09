from django.shortcuts import render, redirect

from home.forms import doctorlogin
from home.models import doctor, Feedback


def doctordashboard(request):
    return render(request, 'doctor/doctorbase.html')


def doc_view_feedback(request):
    data = Feedback.objects.all()
    return render(request, 'doctor/doc_view_feedback.html', {'data': data})
