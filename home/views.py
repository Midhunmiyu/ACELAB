from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from home.forms import loginform, doctorlogin, patientlogin


# Create your views here.
def index(request):
    return render(request, 'index.html')


def doctor_registration(request):
    form1 = loginform()
    form2 = doctorlogin()

    if request.method == 'POST':
        form1 = loginform(request.POST)
        form2 = doctorlogin(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_doctor = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()
            return redirect('login_view')

    return render(request, 'doctor/doctor_registration.html', {'form1': form1, 'form2': form2})


def patient_registration(request):
    form1 = loginform()
    form2 = patientlogin()

    if request.method == 'POST':
        form1 = loginform(request.POST)
        form2 = patientlogin(request.POST)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_patient = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()
            return redirect('login_view')

    return render(request, 'patient/patient_registration.html', {'form1': form1, 'form2': form2})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admindashboard')
            elif user.is_doctor:
                return redirect('doctordashboard')
            elif user.is_patient:
                return redirect('patientdashboard')

        else:
            messages.info(request, 'invalid Credentials')
    return render(request, 'login.html')


def department(request):
    return render(request, 'login.html')


def contact(request):
    return render(request, 'login.html')
