from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views, adminview, doctorviews, patientviews

urlpatterns = [
    path('', views.index, name='index'),
    path('doctor_registration', views.doctor_registration, name='doctor_registration'),
    path('patient_registration', views.patient_registration, name='patient_registration'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),


    # admin urls

    path('add_department', adminview.add_department, name='add_department'),
    path('admindashboard', adminview.admindashboard, name='admindashboard'),
    path('view_department', adminview.view_department, name='view_department'),
    path('delete/<int:id>/', adminview.delete, name='delete'),
    path('doc_view', adminview.doc_view, name='doc_view'),
    path('update/<int:pk>/', adminview.update, name='update'),
    path('doc_delete/<int:pk>/', adminview.doc_delete, name='doc_delete'),
    path('view_patient', adminview.view_patient, name='view_patient'),
    path('update_patient/<int:id>/', adminview.update_patient, name='update_patient'),
    path('delete_patient/<int:id>/', adminview.delete_patient, name='delete_patient'),
    path('doc_notification', adminview.doc_notification, name='doc_notification'),
    path('pat_notification', adminview.pat_notification, name='pat_notification'),
    path('view_pat_notifications', adminview.view_pat_notifications, name='view_pat_notifications'),
    path('view_doc_notifications', adminview.view_doc_notifications, name='view_doc_notifications'),
    path('delete_docnotification/<int:id>/', adminview.delete_docnotification, name='delete_docnotification'),
    path('delete_patnotification/<int:id>/', adminview.delete_patnotification, name='delete_patnotification'),
    path('admin_view_feedbacks', adminview.admin_view_feedbacks, name='admin_view_feedbacks'),
    path('reply_feedback/<int:id>/', adminview.reply_feedback, name='reply_feedback'),
    path('add_schedule', adminview.add_schedule, name='add_schedule'),
    path('view_schedule', adminview.view_schedule, name='view_schedule'),
    path('delete_schedule/<int:id>/', adminview.delete_schedule, name='delete_schedule'),
    path('booking_view', adminview.booking_view, name='booking_view'),
    path('approve_app/<int:id>/', adminview.approve_app, name='approve_app'),
    path('reject_app/<int:id>/', adminview.reject_app, name='reject_app'),
    path('doc_approval_list', adminview.doc_approval_list, name='doc_approval_list'),
    path('approve_doc/<int:user_id>/', adminview.approve_doc, name='approve_doc'),
    path('reject_doc/<int:user_id>/', adminview.reject_doc, name='reject_doc'),

    # doctor urls

    path('doctordashboard', doctorviews.doctordashboard, name='doctordashboard'),
    path('doc_view_feedback', doctorviews.doc_view_feedback, name='doc_view_feedback'),
    path('doc_view_appointments', doctorviews.doc_view_appointments, name='doc_view_appointments'),
    path('doc_view_patients', doctorviews.doc_view_patients, name='doc_view_patients'),
    path('doc_view_notificaction', doctorviews.doc_view_notificaction, name='doc_view_notificaction'),
    path('view_patient_data', doctorviews.view_patient_data, name='view_patient_data'),


    # patient urls

    path('patientdashboard', patientviews.patientdashboard, name='patientdashboard'),
    path('patient_view_department', patientviews.patient_view_department, name='patient_view_department'),
    path('patient_view_doctor', patientviews.patient_view_doctor, name='patient_view_doctor'),
    path('AddFeedback', patientviews.AddFeedback, name='AddFeedback'),
    path('view_feedback', patientviews.view_feedback, name='view_feedback'),
    path('patient_view_notification', patientviews.patient_view_notification, name='patient_view_notification'),
    path('patient_view_schedule', patientviews.patient_view_schedule, name='patient_view_schedule'),
    path('book_apppointment/<int:id>/', patientviews.book_apppointment, name='book_apppointment'),
    path('appointment_view', patientviews.appointment_view, name='appointment_view'),
    path('patient_data', patientviews.patient_data, name='patient_data'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)