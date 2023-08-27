from django.shortcuts import render
from . models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import mixins,generics

# Create your views here.

class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class CourseDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request , pk)
'''
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course , many=True)
        return Response(serializer.data)
    
    def post(self, request):
        courseserializer = CourseSerializer(data = request.data)
        if courseserializer.is_valid():
            courseserializer.save()
            return Response(courseserializer.data , status=status.HTTP_201_CREATED)
        return Response(courseserializer.errors)
    

class CourseDetailView(APIView):
    
    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self , request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self , request, pk):
        course = self.get_course(pk)
        courseserializer = CourseSerializer(course, data = request.data)
        if courseserializer.is_valid():
            courseserializer.save()
            return Response(courseserializer.data)
        return Response(courseserializer.errors)

    def delete(self , request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
