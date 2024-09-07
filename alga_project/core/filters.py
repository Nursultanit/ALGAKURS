import django_filters
from .models import (
    ALGA_Department, Professor, Student, Course, Office, Schedule, CourseRegistration
)

class ALGA_DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = ALGA_Department
        fields = ['name', 'description']

class ProfessorFilter(django_filters.FilterSet):
    class Meta:
        model = Professor
        fields = ['user__first_name', 'user__last_name', 'title', 'department']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['user__first_name', 'user__last_name', 'department']

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'department', 'professor']

class OfficeFilter(django_filters.FilterSet):
    class Meta:
        model = Office
        fields = ['room_number', 'building']

class ScheduleFilter(django_filters.FilterSet):
    class Meta:
        model = Schedule
        fields = ['course', 'day_of_week']

class CourseRegistrationFilter(django_filters.FilterSet):
    class Meta:
        model = CourseRegistration
        fields = ['student', 'course']
