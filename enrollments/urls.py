from django.urls import path
from . import views

urlpatterns = [
    path('', views.EnrollmentListCreateView.as_view(), name='enrollments_list_create'),
    path('<int:pk>/', views.EnrollmentRetrieveUpdateDeleteView.as_view(), name='enrollments_detail'),
]
