from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class School(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 200)
    district = models.CharField(max_length = 200)
    code = models.CharField(max_length = 20)
    logo = models.ImageField(default = 'default.jpg', upload_to='school_logos')

class staff(models.Model):
    STAFF_CHOICES = (
        ('T', 'Teacher'),
        ('A', 'Admin'),
        ('M', 'Maintanance'),
        ('D', 'Driver'),

        )
    position = models.CharField(max_length = 1, default = "T", null = True, choices = STAFF_CHOICES)
    salary = models.IntegerField(null = True)

class Teacher(models.Model):
   
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'Female'),
    )
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




class Student(models.Model):
   
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'Female'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 50, null = True)
    photo = models.ImageField(default = 'default.jpg', null = True, upload_to = 'student_img')
    gender = models.CharField(max_length = 1, null = True, choices = GENDER_CHOICES)
    DOB = models.DateField(null = True)
    std = models.CharField(max_length = 50, null = True)
    mobile_no = models.IntegerField(null = True, default=2022)
    email_id = models.EmailField(max_length = 254, default = "a@gmail.com", null = True)
    address = models.TextField(null = True)



    def __str__(self):
        return self.name

class StudentAttendance(models.Model):
    ATTENDANCE_CHOICES = (
        ('P', 'Present'),
        ('A', 'Absent'),
    )
    student = models.ForeignKey(Student, on_delete = models.CASCADE, blank = True, null = True)
    attendance = models.CharField(max_length = 1, null = True, choices = ATTENDANCE_CHOICES)

class StaffAttendance(models.Model):
    ATTENDANCE_CHOICES = (
        ('P', 'Present'),
        ('A', 'Absent'),
    )

    staff = models.ForeignKey(staff, on_delete = models.CASCADE, blank = True, null = True)
    attendance = models.CharField(max_length = 1, null = True, choices = ATTENDANCE_CHOICES)


class Transport(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    pickup_location = models.CharField(max_length = 50)
    drop_location = models.CharField(max_length = 50)
    fees = models.IntegerField(null = True)
