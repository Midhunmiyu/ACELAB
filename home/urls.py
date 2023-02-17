from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('doctor_registration',views.doctor_registration,name='doctor_registration'),
    path('patient_registration',views.patient_registration,name='patient_registration'),

]