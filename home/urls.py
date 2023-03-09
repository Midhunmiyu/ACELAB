from django.conf import settings
from django.conf.urls.static import static
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
    path('view_pat_notifications', adminview.view_pat_notifications, name='view_pat_notifications'),
    path('view_doc_notifications', adminview.view_doc_notifications, name='view_doc_notifications'),
    path('delete_docnotification/<int:id>/', adminview.delete_docnotification, name='delete_docnotification'),
    path('delete_patnotification/<int:id>/', adminview.delete_patnotification, name='delete_patnotification'),
    path('admin_view_feedbacks', adminview.admin_view_feedbacks, name='admin_view_feedbacks'),
    path('reply_feedback/<int:id>/', adminview.reply_feedback, name='reply_feedback'),


    # doctor urls

    path('doctordashboard', doctorviews.doctordashboard, name='doctordashboard'),


    # patient urls

    path('patientdashboard', patientviews.patientdashboard, name='patientdashboard'),
    path('patient_view_department', patientviews.patient_view_department, name='patient_view_department'),
    path('patient_view_doctor', patientviews.patient_view_doctor, name='patient_view_doctor'),
    path('AddFeedback', patientviews.AddFeedback, name='AddFeedback'),
    path('view_feedback', patientviews.view_feedback, name='view_feedback'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)