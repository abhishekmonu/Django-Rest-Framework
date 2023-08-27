
from django.urls import path
from . views import CourseListView,InstructorListView

urlpatterns = [
    path("Instructor/",InstructorListView.as_view()),
    path("Course/",CourseListView.as_view()),

    # path("coursedetail/<int:pk>",CourseDetailView.as_view()),

]
