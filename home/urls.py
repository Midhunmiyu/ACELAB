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
    path('doc_view', adminview.doc_view, name='doc_view'),
    path('update/<int:id>/', adminview.update, name='update'),
    path('doc_delete/<int:id>/', adminview.doc_delete, name='doc_delete'),
    path('view_patient', adminview.view_patient, name='view_patient'),
    path('update_patient/<int:id>/', adminview.update_patient, name='update_patient'),
    path('delete_patient/<int:id>/', adminview.delete_patient, name='delete_patient'),
    path('doc_notification', adminview.doc_notification, name='doc_notification'),
    path('pat_notification', adminview.pat_notification, name='pat_notification'),
    path('view_notifications', adminview.view_notifications, name='view_notifications'),


    # doctor urls

    path('doctordashboard', doctorviews.doctordashboard, name='doctordashboard'),


    # patient urls

    path('patientdashboard', patientviews.patientdashboard, name='patientdashboard'),



]
