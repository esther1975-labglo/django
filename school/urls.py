from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school import views
from .views import (
    UserViewSet, 
    SchoolViewSet,
    StaffViewSet,
    TeacherViewSet,
    StudentViewSet,
    TransportViewSet,
    StudentAttendanceViewSet,
    StaffAttendanceViewSet, 
    RegisterAPI
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'school', SchoolViewSet)
router.register(r'staffs', StaffViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'transport', TransportViewSet)
router.register(r'StudentAttendance', StudentAttendanceViewSet)
router.register(r'StaffAttendance', StaffAttendanceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginView.as_view()),
]