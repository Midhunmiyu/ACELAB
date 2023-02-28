from django.shortcuts import render, redirect

from home.forms import patientlogin
from home.models import patient


def patientdashboard(request):
    return render(request, 'patient/patientbase.html')


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
        form = patientlogin(request, instance=id)
        if form.is_valid():
            form.save()
            return redirect('view_patient')
    return render(request, 'admin1/update_patient.html', {'form': form})
