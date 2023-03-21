from django import forms
from django.contrib.auth.forms import UserCreationForm

from home.models import Login, doctor, patient, department, DoctorNotification, PatientNotification, Feedback, \
    DocSchedule


class loginform(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class doctorlogin(forms.ModelForm):
    class Meta:
        model = doctor
        fields = '__all__'
        exclude = ('user',)


class patientlogin(forms.ModelForm):
    class Meta:
        model = patient
        fields = '__all__'
        exclude = ('user',)


class departmentform(forms.ModelForm):
    class Meta:
        model = department
        fields = '__all__'


class DoctorNotificationForm(forms.ModelForm):
    class Meta:
        model = DoctorNotification
        fields = '__all__'


class PatientNotificationForm(forms.ModelForm):
    class Meta:
        model = PatientNotification
        fields = '__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = ('reply', 'user',)


class AdminFeedback(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = ('user',)


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ScheduleForm(forms.ModelForm):
    Date = forms.DateField(widget=DateInput)
    Start_time = forms.TimeField(widget=TimeInput)
    End_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = DocSchedule
        fields = ('Doc_name','Date','Start_time','End_time')
