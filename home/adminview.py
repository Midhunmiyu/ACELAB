from django.shortcuts import redirect, render
from home.forms import departmentform, doctorlogin, patientlogin, DoctorNotificationForm, PatientNotificationForm, \
    FeedbackForm, AdminFeedback

from home.models import department, doctor, patient, DoctorNotification, PatientNotification, Feedback


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
    form = AdminFeedback(instance=data)
    if request.method == 'POST':
        form = AdminFeedback(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('admin_view_feedbacks')
    return render(request, 'admin1/reply_feedback.html', {'form': form})
