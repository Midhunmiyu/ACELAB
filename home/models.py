from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Login(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


class doctor(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class patient(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.TextField()

    def __str__(self):
        return self.dept_name
