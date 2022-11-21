from django.contrib import admin
from school.models import (
    School,
    staff,
    Teacher,
    Student,
    Class,
    StudentAttendance,
    StaffAttendance,
    Transport
)


admin.site.register(Student)
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(staff)
admin.site.register(Transport)
admin.site.register(StudentAttendance)
admin.site.register(StaffAttendance)



