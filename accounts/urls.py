from django.urls import path
from . import views

urlpatterns= [
    path('home/', views.home),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('patient/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/display_users', views.display_users, name='display_users'),
    path('admin/add_users', views.add_users, name='add_users'),
    path('patient/book_appointment_patient/', views.book_appointment_patient, name='book_appointment_patient'),
    path('patient/display_appointments/', views.display_appointments, name='display_appointments'),
    path('doctor/manage_availability/', views.manage_availability, name='manage_availability'),
    path('doctor/display_timeslots/', views.display_timeslots, name='display_timeslots'),
    path('doctor/display_patients_appointments/', views.display_patients_appointments, name='display_patients_appointments'),
]