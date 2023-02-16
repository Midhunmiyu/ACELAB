from django import forms
from django.contrib.auth.forms import UserCreationForm

from home.models import Login, doctor, patient


class loginform(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class doctorlogin(UserCreationForm):

    class Meta:
        model = doctor
        fields = '__all__'
        exclude = ' user'


class patientlogin(UserCreationForm):

    class Meta:
        model = patient
        fields = '__all__'
        exclude = ' user'
