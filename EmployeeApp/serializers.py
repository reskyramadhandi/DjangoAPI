from rest_framework import serializers
from EmployeeApp.models import Departments, Employees, Grades


class DepartmentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId', 'DepartmentName')


class GradeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ('GradeId', 'GradeName')


class EmployeeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'DateOfJoining',
                  'PhotoFileName', 'DepartmentId')
