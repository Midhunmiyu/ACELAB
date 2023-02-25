from django.shortcuts import render


def patientdashboard(request):
    return render(request,'patient/patientbase.html')