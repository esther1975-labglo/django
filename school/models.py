from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

ATTENDANCE_CHOICES = (
        ('P', 'Present'),
        ('A', 'Absent'),
    )

STAFF_CHOICES = (
        ('T', 'Teacher'),
        ('A', 'Admin'),
        ('M', 'Maintanance'),
        ('D', 'Driver'),
    )


class Timestamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class School(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 200)
    district = models.CharField(max_length = 200)
    code = models.CharField(max_length = 20)
    logo = models.ImageField(default = 'default.jpg', upload_to='school_logos')


class staff(models.Model):
    position = models.CharField(max_length = 1, default = "T", null = True, choices = STAFF_CHOICES)
    salary = models.IntegerField(null = True)


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 50, null = True)
    photo = models.ImageField(default = 'default.jpg', null = True, upload_to = 'student_img')
    gender = models.CharField(max_length = 1, null = True, choices = GENDER_CHOICES)
    DOB = models.DateField(null = True)
    subject = models.CharField(max_length = 50, null = True)
    mobile_no = models.IntegerField(null = True, default=2022)
    email_id = models.EmailField(max_length = 254, default = "@gmail.com", null = True)
    address = models.TextField(null = True)
  
    def __str__(self):
        return self.name


class Class(models.Model):
    class_name = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 

    def __str__(self):
        return self.class_name


class Student(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 50, null = True)
    photo = models.ImageField(default = 'default.jpg', null = True, upload_to = 'student_img')
    gender = models.CharField(max_length = 1, null = True, choices = GENDER_CHOICES)
    DOB = models.DateField(null = True)
    standard = models.CharField(max_length = 50, null = True)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, blank = True, null = True)
    mobile_no = models.IntegerField(null = True, default=2022)
    email_id = models.EmailField(max_length = 254, default = "a@gmail.com", null = True)
    address = models.TextField(null = True)

    def __str__(self):
        return self.name


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, blank = True, null = True)
    attendance = models.CharField(max_length = 1, null = True, choices = ATTENDANCE_CHOICES)


class StaffAttendance(models.Model):
    staff = models.ForeignKey(staff, on_delete = models.CASCADE, blank = True, null = True)
    attendance = models.CharField(max_length = 1, null = True, choices = ATTENDANCE_CHOICES)


class Transport(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    pickup_location = models.CharField(max_length = 50)
    drop_location = models.CharField(max_length = 50)
    fees = models.IntegerField(null = True)
