from django.contrib import admin

from .models import Course, ClassSession

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'duration_hours', 'price', 'created_at']
    search_fields = ['name', 'code', 'description']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(ClassSession)
class ClassSessionAdmin(admin.ModelAdmin):
    list_display = ['course', 'title', 'instructor_id', 'instructor_name', 'start_time', 'created_at']
    search_fields = ['title', 'instructor_name', 'location']
    readonly_fields = ['created_at', 'updated_at']

