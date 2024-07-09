from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class employee_viewset(APIView):

    def get(self, request, id=None):
        try:
            if id:
                employee = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(employee)
                return Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
            
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"status": "error", "data": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    

    def post(self, request):
       serializer = EmployeeSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
       else:
          return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
       
    def patch(self, request, id=None):
        try:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({"status": "error", "data": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id=None):
        try:
            employee = Employee.objects.filter(id=id)
            employee.delete()
            return Response({"status": "sucess", "data": "Data Deleted"}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"status": "error", "data": "Data Not Found"}, status=status.HTTP_400_BAD_REQUEST)