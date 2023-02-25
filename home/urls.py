from django.urls import path
from . import views, adminview, doctorviews, patientviews

urlpatterns = [
    path('', views.index, name='index'),
    path('doctor_registration', views.doctor_registration, name='doctor_registration'),
    path('patient_registration', views.patient_registration, name='patient_registration'),
    path('add_department', adminview.add_department, name='add_department'),
    path('admindashboard', adminview.admindashboard, name='admindashboard'),
    path('view_department', adminview.view_department, name='view_department'),
    path('delete/<int:id>/', adminview.delete, name='delete'),
    path('login_view', views.login_view, name='login_view'),
    path('doctordashboard', doctorviews.doctordashboard, name='doctordashboard'),
    path('patientdashboard', patientviews.patientdashboard, name='patientdashboard'),

]
