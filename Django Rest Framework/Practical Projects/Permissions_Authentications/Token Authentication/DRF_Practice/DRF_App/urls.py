
from django.urls import path
from . views import CourseListView,InstructorListView,CourseDetailView,InstructorDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("Instructor/",InstructorListView.as_view()),
    path("Course/",CourseListView.as_view()),
    path("Course/<int:pk>", CourseDetailView.as_view(), name='course-detail'),
    path("Instructor/<int:pk>", InstructorDetailView.as_view(), name='instructor-detail'),

    # path("coursedetail/<int:pk>",CourseDetailView.as_view()),
    path('auth/login/', obtain_auth_token, name='create-token')
]
