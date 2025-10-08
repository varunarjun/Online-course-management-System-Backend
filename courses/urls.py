from django.urls import path
from . import views

urlpatterns = [
    # CRUD endpoints
    path('', views.CourseListCreateView.as_view(), name='courses_list_create'),
    path('<int:pk>/', views.CourseRetrieveUpdateDestroyView.as_view(), name='courses_detail'),
    path('<int:pk>/analytics/', views.CourseAnalyticsView.as_view(), name='course_analytics'),

    # Admin analytics endpoint
    path('analytics/admin/', views.admin_courses_analytics, name='admin_courses_analytics'),
]
