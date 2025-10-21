from django.db import models

class Student(models.Model):
    STUDENT_FACULTY = [
        ('engineering', 'Engineering'),
        ('science', 'Science'),
        ('business', 'Business'),
        ('arts', 'Arts'),
        ('medicine', 'Medicine'),
    ]
    
    student_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    faculty = models.CharField(max_length=20, choices=STUDENT_FACULTY)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['student_id']