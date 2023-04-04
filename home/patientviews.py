from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from home.forms import FeedbackForm, PatientDataForm
from home.models import department, doctor, Feedback, PatientNotification, DocSchedule, patient, Appointment, \
    PatientData


@login_required(login_url='login_view')
def patientdashboard(request):
    total = PatientNotification.objects.all().count()
    return render(request, 'patient/patientbase.html', {'total': total})


@login_required(login_url='login_view')
def patient_view_department(request):
    data = department.objects.all()
    return render(request, 'patient/view_departments.html', {'data': data})


@login_required(login_url='login_view')
def patient_view_doctor(request):
    data = doctor.objects.all()
    return render(request, 'patient/view_doctors.html', {'data': data})


@login_required(login_url='login_view')
def AddFeedback(request):
    form = FeedbackForm()
    u = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = u
            a.save()
            return redirect('view_feedback')
    return render(request, 'patient/AddFeedback.html', {'form': form})


@login_required(login_url='login_view')
def view_feedback(request):
    data = Feedback.objects.all()
    return render(request, 'patient/viewfeedback.html', {'data': data})


@login_required(login_url='login_view')
def patient_view_notification(request):
    data = PatientNotification.objects.all()
    return render(request, 'patient/patient_view_notification.html', {'data': data})


@login_required(login_url='login_view')
def patient_view_schedule(request):
    data = DocSchedule.objects.all()
    return render(request, 'patient/viewschedule.html', {'data': data})


@login_required(login_url='login_view')
def book_apppointment(request, id):
    data = DocSchedule.objects.get(id=id)
    p = patient.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=p, Schedule=data)
    if appointment.exists():
        messages.info(request, 'You have already requested for this slot')
        return redirect('patient_view_schedule')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = p
            obj.Schedule = data
            obj.save()
            messages.info(request, 'appointment successful..!!')
            return redirect('appointment_view')
    return render(request, 'patient/Bookappointment.html', {'data': data})


@login_required(login_url='login_view')
def appointment_view(request):
    p = patient.objects.get(user=request.user)
    data = Appointment.objects.filter(user=p)
    return render(request, 'patient/appointment_view.html', {'data': data})


@login_required(login_url='login_view')
def patient_data(request):
    form = PatientDataForm()
    u = request.user
    if request.method == 'POST':
        form = PatientDataForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'The data sent Successfully..!!')
            return redirect('patient_data')
    return render(request, 'patient/patient_data.html', {'form': form})
