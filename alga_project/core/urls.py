from django.urls import path
from .views import (
    ALGA_DepartmentListCreate, ALGA_DepartmentDetail,
    ProfessorListCreate, ProfessorDetail,
    StudentListCreate, StudentDetail,
    CourseListCreate, CourseDetail,
    OfficeListCreate, OfficeDetail,
    ScheduleListCreate, ScheduleDetail,
    CourseRegistrationListCreate, CourseRegistrationDetail,
)

urlpatterns = [
    path('', ALGA_DepartmentListCreate.as_view(), name='department-list-create'),
    path('<int:pk>/', ALGA_DepartmentDetail.as_view(), name='department-detail'),

    path('professors/', ProfessorListCreate.as_view(), name='professor-list-create'),
    path('professors/<int:pk>/', ProfessorDetail.as_view(), name='professor-detail'),

    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),

    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),

    path('offices/', OfficeListCreate.as_view(), name='office-list-create'),
    path('offices/<int:pk>/', OfficeDetail.as_view(), name='office-detail'),

    path('schedules/', ScheduleListCreate.as_view(), name='schedule-list-create'),
    path('schedules/<int:pk>/', ScheduleDetail.as_view(), name='schedule-detail'),

    path('registrations/', CourseRegistrationListCreate.as_view(), name='registration-list-create'),
    path('registrations/<int:pk>/', CourseRegistrationDetail.as_view(), name='registration-detail'),
]
