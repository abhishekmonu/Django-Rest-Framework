from django.shortcuts import render
from rest_framework import generics
from . serializers import InstructorSerializer,CourseSerializer
from . models import Instructor,Course
from rest_framework.permissions import IsAuthenticated, BasePermission , IsAdminUser
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)

    
class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return True

        if request.method == "POST" or request.method == "PUT" or request.method == "DELETE":
            if user.is_superuser:
                return True
        return False

class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class CourseListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,WriteByAdminOnlyPermission]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
