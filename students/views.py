# students/views.py
from rest_framework import viewsets, filters
from .models import Student
from .serializers import StudentSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer
        filter_backends = [filters.SearchFilter, filters.OrderingFilter]
        search_fields = ['student_id', 'first_name', 'last_name', 'faculty']
        ordering_fields = ['student_id', 'first_name', 'gpa', 'created_at']
        ordering = ['student_id']