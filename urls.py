from django.urls import path
from . import views

app_name = 'course_mgmt'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Navigation tab aliases
    path('classes/', views.dashboard, name='classes'),


    # Course
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/<uuid:pk>/edit/', views.course_edit, name='course_edit'),
    path('courses/<uuid:pk>/delete/', views.course_delete, name='course_delete'),
    path('courses/<uuid:pk>/toggle/', views.course_toggle_status, name='course_toggle_status'),
    path('courses/bulk/', views.courses_bulk_action, name='courses_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
