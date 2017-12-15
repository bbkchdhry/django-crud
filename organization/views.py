from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Organization, Department
from .serializers import OrganizationSerializer, DepartmentSerializer


class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# @api_view(['GET', 'POST'])
# def department_list(request):
#     if request.method == 'GET':
#         department = Department.objects.all()
#         serializer = DepartmentSerializer(department, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = DepartmentSerializer(data=request.data)
#         if serializer.is_valid():
#             print("serializer valid")
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
