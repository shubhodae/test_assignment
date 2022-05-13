from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

class EmployeeView(APIView):

    def post(self, request):
        data = {
            "name": request.data.get("name"),
            "phone": request.data.get("phone"),
            "address": request.data.get("address")
        }
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        employees = Employee.objects.all()
        serialize = EmployeeSerializer(employees, many=True)

        return Response(serialize.data, status = status.HTTP_200_OK)


class EmployeeDetailView(APIView):

    def put(self, request, emp_id):
        employee_obj = Employee.objects.filter(id=emp_id).first()
        if not emp_id:
            return Response({
                "message": "employee does not exists"
            }, status = status.HTTP_404_NOT_FOUND)

        data = {
            "name": request.data.get("name"),
            "phone": request.data.get("phone"),
            "address": request.data.get("address")
        }
        serializer = EmployeeSerializer(instance=employee_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, emp_id):
        employee_obj = get_object_or_404(Employee, pk=emp_id)
        serialize = EmployeeSerializer(employee_obj)

        return Response(serialize.data, status = status.HTTP_200_OK)

    def delete(self, request, emp_id):
        employee_obj = Employee.objects.filter(id=emp_id).first()
        if not employee_obj:
            return Response({
                "message": "employee does not exists"
            }, status = status.HTTP_404_NOT_FOUND)
        employee_obj.delete()
        return Response({
            "message": "Employee deleted"
        }, status = status.HTTP_200_OK)
