from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ('id', 'firstName', 'lastName','age','mobile','email','address','images')
        fields = '__all__'