
from django.urls import path
from . views import CourseListView,InstructorListView,CourseDetailView,InstructorDetailView

urlpatterns = [
    path("Instructor/",InstructorListView.as_view()),
    path("Course/",CourseListView.as_view()),
    path("Course/<int:pk>", CourseDetailView.as_view(), name='course-detail'),
    path("Instructor/<int:pk>", InstructorDetailView.as_view(), name='instructor-detail'),

    # path("coursedetail/<int:pk>",CourseDetailView.as_view()),

]
