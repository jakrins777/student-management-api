# สร้างไฟล์ students/management/commands/seed_data.py
import os
import django
from django.core.management.base import BaseCommand
from students.models import Student

class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **options):
        sample_students = [
            {
                'student_id': '6631000001',
                'first_name': 'สมชาย',
                'last_name': 'ใจดี',
                'email': 'somchai.j@example.com',
                'faculty': 'engineering',
                'gpa': 3.25
            },
            {
                'student_id': '6631000002', 
                'first_name': 'สุนิสา',
                'last_name': 'ศรีสุข',
                'email': 'sunisa.s@example.com',
                'faculty': 'science',
                'gpa': 3.75
            },
            {
                'student_id': '6631000003',
                'first_name': 'อนุชา',
                'last_name': 'ทองแท้',
                'email': 'anucha.t@example.com', 
                'faculty': 'business',
                'gpa': 2.95
            }
        ]
        
        for student_data in sample_students:
            student, created = Student.objects.get_or_create(
                student_id=student_data['student_id'],
                defaults=student_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created student: {student.student_id}')
                )