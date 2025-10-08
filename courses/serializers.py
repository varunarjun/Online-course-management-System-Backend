from rest_framework import serializers
from .models import Course
from enrollments.models import Enrollment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # include all fields


class CourseAnalyticsSerializer(serializers.ModelSerializer):
    total_enrollments = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'total_enrollments']

    def get_total_enrollments(self, obj):
        return Enrollment.objects.filter(course=obj).count()
