from django.db import models

# Create your models here.


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)


class Grades(models.Model):
    GradeId = models.AutoField(primary_key=True)
    GradeName = models.CharField(max_length=500)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
    DepartmentId = models.IntegerField()
    GradeId = models.IntegerField()
