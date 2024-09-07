from django.shortcuts import render
from rest_framework import generics, filters
from .models import (
    ALGA_Department, Professor, Student, Course, Office, Schedule, CourseRegistration
)
from .serializers import (
    ALGA_DepartmentSerializer, ProfessorSerializer, StudentSerializer,
    CourseSerializer, OfficeSerializer, ScheduleSerializer, CourseRegistrationSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
from .filters import (
    ALGA_DepartmentFilter, ProfessorFilter, StudentFilter,
    CourseFilter, OfficeFilter, ScheduleFilter, CourseRegistrationFilter
)

class ALGA_DepartmentListCreate(generics.ListCreateAPIView):
    queryset = ALGA_Department.objects.all()
    serializer_class = ALGA_DepartmentSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    filterset_class = ALGA_DepartmentFilter

class ALGA_DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ALGA_Department.objects.all()
    serializer_class = ALGA_DepartmentSerializer


class ProfessorListCreate(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['user__first_name', 'user__last_name', 'title']
    filterset_class = ProfessorFilter

class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['user__first_name', 'user__last_name']
    filterset_class = StudentFilter

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'code', 'description']
    filterset_class = CourseFilter

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class OfficeListCreate(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['room_number', 'building']
    filterset_class = OfficeFilter

class OfficeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class ScheduleListCreate(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['course__name', 'classroom__room_number']
    filterset_class = ScheduleFilter

class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class CourseRegistrationListCreate(generics.ListCreateAPIView):
    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['student__user__first_name', 'student__user__last_name', 'course__name']
    filterset_class = CourseRegistrationFilter

class CourseRegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
