from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_registration, name='student_registration'),
    path('', views.ajax_register, name='ajax_register'),
    path('', views.export_students_csv, name='export_students_csv'),
    path('', views.export_students_pdf, name='export_students_pdf'),
]
