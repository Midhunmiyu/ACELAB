from django.urls import path
from . import views, adminview, doctorviews, patientviews

urlpatterns = [
    path('', views.index, name='index'),
    path('doctor_registration', views.doctor_registration, name='doctor_registration'),
    path('patient_registration', views.patient_registration, name='patient_registration'),
    path('login_view', views.login_view, name='login_view'),

    # admin urls

    path('add_department', adminview.add_department, name='add_department'),
    path('admindashboard', adminview.admindashboard, name='admindashboard'),
    path('view_department', adminview.view_department, name='view_department'),
    path('delete/<int:id>/', adminview.delete, name='delete'),


    # doctor urls

    path('doctordashboard', doctorviews.doctordashboard, name='doctordashboard'),
    path('doc_view', doctorviews.doc_view, name='doc_view'),
    path('update/<int:id>/', doctorviews.update, name='update'),
    path('doc_delete/<int:id>/', doctorviews.doc_delete, name='doc_delete'),

    # patient urls

    path('patientdashboard', patientviews.patientdashboard, name='patientdashboard'),
    path('view_patient', patientviews.view_patient, name='view_patient'),
    path('update_patient/<int:id>/', patientviews.update_patient, name='update_patient'),
    path('delete_patient/<int:id>/', patientviews.delete_patient, name='delete_patient'),


]
