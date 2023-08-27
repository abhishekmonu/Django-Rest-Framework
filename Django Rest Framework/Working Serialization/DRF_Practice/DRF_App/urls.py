
from django.urls import path
from . views import CourseListView,InstructorListView,CourseDetailView,InstructorDetailView
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path("Instructor/",InstructorListView.as_view()),
    path("Course/",CourseListView.as_view()),
    path("Course/<int:pk>", CourseDetailView.as_view(), name='course-detail'),
    path("Instructor/<int:pk>", InstructorDetailView.as_view(), name='instructor-detail'),
    path('auth/login/', TokenObtainPairView.as_view(), name='create-token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]
