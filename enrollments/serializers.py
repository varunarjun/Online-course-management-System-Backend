from rest_framework import serializers
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        # Use 'student' instead of 'user'
        fields = [
            'id', 
            'student', 
            'course', 
            'progress_status', 
            'payment_status', 
            'transaction_id', 
            'enrolled_at'
        ]
