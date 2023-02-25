from django.shortcuts import render


def doctordashboard(request):
    return render(request,'doctor/doctorbase.html')