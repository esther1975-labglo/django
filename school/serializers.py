from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from school.models import *
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        token = serializers.SerializerMethodField('get_user_token')

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'])

        return user

    def get_user_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('url', 'name', 'user', 'district', 'code')

class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = staff
        fields = ('url', 'position', 'salary')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'name', 'user', 'gender', 'photo', 'DOB', 'subject', 'mobile_no', 'email_id', 'address')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'name', 'user', 'gender', 'photo', 'DOB', 'std', 'mobile_no', 'email_id', 'address')

class TransportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transport
        fields = ('url', 'user', 'pickup_location', 'drop_location', 'fees')

class StaffAttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = ('url', 'staff', 'attendance')

class StudentAttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = ('url', 'student', 'attendance')



