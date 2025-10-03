# enrollments/models.py
from django.db import models
from users.models import User
from courses.models import Course
from django.utils import timezone


class Enrollment(models.Model):
    PROGRESS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    PAYMENT_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress_status = models.CharField(max_length=20, choices=PROGRESS_CHOICES, default='not_started')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    enrolled_at = models.DateTimeField(auto_now_add=True, default=timezone.now)

    def __str__(self):
        return f"{self.student.email} - {self.course.title}"
