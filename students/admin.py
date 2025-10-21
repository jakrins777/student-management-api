# students/admin.py
from django.contrib import admin
from .models import Student


    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
        list_display = ('student_id', 'first_name', 'last_name', 'faculty', 'gpa', 'created_at')
        list_filter = ('faculty', 'created_at')
        search_fields = ('student_id', 'first_name', 'last_name')
        ordering = ('student_id',)