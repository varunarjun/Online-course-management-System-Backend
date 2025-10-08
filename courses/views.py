from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer, CourseAnalyticsSerializer
from enrollments.models import Enrollment

# ---------------------------------------
# Admin: Analytics for all courses
# ---------------------------------------
@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_courses_analytics(request):
    """
    Returns analytics for all courses:
    - Total enrollments
    - Revenue collected (completed payments only)
    - Progress breakdown
    """
    courses = Course.objects.all()
    result = []

    for course in courses:
        enrollments = Enrollment.objects.filter(course=course)
        total_enrollments = enrollments.count()
        revenue_collected = sum(e.course.fee for e in enrollments if e.payment_status == "completed")

        progress = {
            "not_started": enrollments.filter(progress_status="not_started").count(),
            "in_progress": enrollments.filter(progress_status="in_progress").count(),
            "completed": enrollments.filter(progress_status="completed").count()
        }

        result.append({
            "course_id": course.id,
            "title": course.title,
            "total_enrollments": total_enrollments,
            "revenue_collected": revenue_collected,
            "progress": progress
        })

    return Response(result)


# ---------------------------------------
# CRUD Views for Courses
# ---------------------------------------

# List all courses and create a new course
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


# Retrieve, update, partially update, or delete a single course
class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


# Analytics for a single course
class CourseAnalyticsView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseAnalyticsSerializer
    permission_classes = [IsAuthenticated]
