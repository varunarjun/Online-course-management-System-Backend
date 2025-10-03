from django.db import models
from users.models import User

class Course(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('approved','Approved'),
        ('rejected','Rejected')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    fee = models.FloatField()
    category = models.CharField(max_length=50)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'instructor'})
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
