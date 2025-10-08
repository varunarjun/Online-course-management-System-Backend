from rest_framework import generics, permissions
from .models import Enrollment
from .serializers import EnrollmentSerializer

# -----------------------------
# List and Create Enrollments
# -----------------------------
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

# -----------------------------
# Retrieve, Update, Delete Enrollment
# -----------------------------
class EnrollmentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]
