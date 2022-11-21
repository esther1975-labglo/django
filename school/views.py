from rest_framework import viewsets
from django.shortcuts import render
from school.models import (
    User,
    School,
    staff,
    Teacher,
    Student,
    Class,
    StudentAttendance,
    StaffAttendance,
    Transport,
    Review
)
from school.serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    SchoolSerializer,
    StaffSerializer,
    TeacherSerializer,
    StudentSerializer,
    ClassSerializer,
    TransportSerializer,
    StaffAttendanceSerializer,
    StudentAttendanceSerializer,
    ReviewSerializer
)
from rest_framework import permissions
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from django.contrib.auth import login
from rest_framework.authentication import TokenAuthentication

'''user registeration'''

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token,created=Token.objects.get_or_create(user=user)
        return Response({
        "token": token.key,    
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        }, status=status.HTTP_200_OK)

'''user login'''

class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_200_OK)

'''user CRUD operation'''

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

'''school CRUD operation'''

class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

'''staff CRUD operation'''

class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = staff.objects.all()

'''teachers CRUD operation'''

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

'''students CRUD operation'''

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

'''student classes CRUD operation'''

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer    

'''transport CRUD operation'''

class TransportViewSet(viewsets.ModelViewSet):
    serializer_class = TransportSerializer
    queryset = Transport.objects.all()

'''attendance CRUD operation'''

class StudentAttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = StudentAttendanceSerializer
    queryset = StudentAttendance.objects.all()

class StaffAttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = StaffAttendanceSerializer
    queryset = StaffAttendance.objects.all()

'''review'''

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()