from django.urls import path
from . import views

app_name = 'course_mgmt'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('courses/', views.courses, name='courses'),
    path('classes/', views.classes, name='classes'),
    path('settings/', views.settings, name='settings'),
]
