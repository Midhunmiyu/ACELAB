from django.contrib import messages
from django.shortcuts import redirect, render
from home.forms import departmentform, doctorlogin, patientlogin, DoctorNotificationForm, PatientNotificationForm, \
    FeedbackForm, AdminFeedback, ScheduleForm

from home.models import department, doctor, patient, DoctorNotification, PatientNotification, Feedback, \
    DocSchedule, Appointment


def admindashboard(request):
    return render(request, 'admin1/admindashboard.html')


def add_department(request):
    form = departmentform()
    if request.method == 'POST':
        form = departmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_department')
    return render(request, 'admin1/adddepartments.html', {'form': form})


def view_department(request):
    data = department.objects.all()
    return render(request, 'admin1/viewdepartments.html', {'data': data})


def delete(request, id):
    data = department.objects.get(id=id)
    data.delete()

    return redirect('view_department')


def doc_view(request):
    data = doctor.objects.all()
    return render(request, 'admin1/doc_list.html', {'data': data})


def doc_delete(request, id):
    data = doctor.objects.get(id=id)
    data.delete()

    return redirect('doc_view')


def update(request, id):
    data = doctor.objects.get(id=id)
    form = doctorlogin(instance=data)
    if request.method == 'POST':
        form = doctorlogin(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('doc_view')
    return render(request, 'admin1/doc_update.html', {'form': form})


def view_patient(request):
    data = patient.objects.all()
    return render(request, 'admin1/view_patient.html', {'data': data})


def delete_patient(request, id):
    data = patient.objects.get(id=id)
    data.delete()

    return redirect('view_patient')


def update_patient(request, id):
    data = patient.objects.get(id=id)
    form = patientlogin(instance=data)
    if request.method == 'POST':
        form = patientlogin(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_patient')
    return render(request, 'admin1/update_patient.html', {'form': form})


def doc_notification(request):
    form = DoctorNotificationForm()
    if request.method == 'POST':
        form = DoctorNotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_doc_notifications')
    return render(request, 'admin1/doc_notification.html', {'form': form})


def pat_notification(request):
    form = PatientNotificationForm()
    if request.method == 'POST':
        form = PatientNotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_pat_notifications')
    return render(request, 'admin1/patient_notification.html', {'form': form})


def view_doc_notifications(request):
    data = DoctorNotification.objects.all()
    return render(request, 'admin1/doc_notification_list.html', {'data': data})


def view_pat_notifications(request):
    data = PatientNotification.objects.all()
    return render(request, 'admin1/view_patient_notifications.html', {'data': data})


def delete_docnotification(request, id):
    data = DoctorNotification.objects.get(id=id)
    data.delete()

    return redirect('view_doc_notifications')


def delete_patnotification(request, id):
    data = PatientNotification.objects.get(id=id)
    data.delete()

    return redirect('view_pat_notifications')


def admin_view_feedbacks(request):
    data = Feedback.objects.all()
    return render(request, 'admin1/viewfeedback.html', {'data': data})


def reply_feedback(request, id):
    data = Feedback.objects.get(id=id)
    # list = AdminFeedback(instance=data)
    if request.method == 'POST':
        r = request.POST.get('reply', )
        data.reply = r

        # list = AdminFeedback(request.POST, instance=data)
        # if data.is_valid():
        data.save()
        return redirect('admin_view_feedbacks')
    return render(request, 'admin1/reply_feedback.html', {'list': data})


def add_schedule(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_schedule')
    return render(request, 'admin1/Addschedule.html', {'form': form})


def view_schedule(request):
    data = DocSchedule.objects.all()
    return render(request, 'admin1/viewschedule.html', {'data': data})


def delete_schedule(request, id):
    data = DocSchedule.objects.get(id=id)
    data.delete()
    return redirect('view_schedule')


def booking_view(request):
    data=Appointment.objects.all()
    return render(request,'admin1/booking_view.html',{'data':data})

def approve_app(request,id):
    data=Appointment.objects.get(id=id)
    data.status=1
    data.save()
    messages.info(request,'Appointment Confirmed')
    return redirect('booking_view')

def reject_app(request,id):
    data=Appointment.objects.get(id=id)
    data.status=2
    data.save()
    messages.info(request,'Appointment Rejected')
    return redirect('booking_view')

