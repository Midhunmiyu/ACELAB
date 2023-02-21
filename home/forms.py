from django import forms
from django.contrib.auth.forms import UserCreationForm

from home.models import Login, doctor, patient, department


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
