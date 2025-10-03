# enrollments/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EnrollmentViewSet

router = DefaultRouter()
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')

# Must wrap router.urls with include() in urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
