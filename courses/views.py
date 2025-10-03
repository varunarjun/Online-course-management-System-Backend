# courses/views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from enrollments.models import Enrollment

class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access by default

    # Optional: restrict certain actions to instructors/admins
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]  # Only admins/instructors
        else:
            permission_classes = [permissions.IsAuthenticated]  # All authenticated users can view
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAdminUser])
    def analytics(self, request, pk=None):
        """
        Custom action to get analytics for a specific course.
        Accessible only by admins.
        """
        course = self.get_object()
        enrollments = Enrollment.objects.filter(course=course)

        data = {
            'total_students': enrollments.count(),
            'completed': enrollments.filter(progress_status='completed').count(),
            'in_progress': enrollments.filter(progress_status='in_progress').count(),
            'not_started': enrollments.filter(progress_status='not_started').count(),
            'revenue': sum([e.course.fee for e in enrollments if e.payment_status == 'completed'])
        }
        return Response(data)
