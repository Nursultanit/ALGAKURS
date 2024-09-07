from django.db import models
from django.contrib.auth.models import User

class ALGA_Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(ALGA_Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f'{self.title} {self.user.get_full_name()}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(ALGA_Department, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField()

    def __str__(self):
        return self.user.get_full_name()

class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    description = models.TextField()
    department = models.ForeignKey(ALGA_Department, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Office(models.Model):
    room_number = models.CharField(max_length=10)
    building = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.building} - {self.room_number}'

class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Office, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)

    def __str__(self):
        return f'{self.course.name} - {self.day_of_week}'

class CourseRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    grade = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return f'{self.student} - {self.course.name}'

