from django.shortcuts import render, redirect

from home.forms import FeedbackForm
from home.models import department, doctor, Feedback


def patientdashboard(request):
    return render(request, 'patient/patientbase.html')


def patient_view_department(request):
    data = department.objects.all()
    return render(request, 'patient/view_departments.html', {'data': data})


def patient_view_doctor(request):
    data = doctor.objects.all()
    return render(request, 'patient/view_doctors.html', {'data': data})


def AddFeedback(request):
    form = FeedbackForm()
    u=request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.user=u
            a.save()
            return redirect('view_feedback')
    return render(request, 'patient/AddFeedback.html', {'form': form})


def view_feedback(request):
    data = Feedback.objects.all()
    return render(request, 'patient/viewfeedback.html', {'data': data})
