from . models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=10)


    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, employee, validated_data):
        newEmployee = Employee(**validated_data)
        newEmployee.id = employee.id
        newEmployee.save()
        return newEmployee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
