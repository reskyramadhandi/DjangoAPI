from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees, Grades
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer, GradeSerializer

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def department_api(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Sucessfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(
            DepartmentId=department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(
            department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Sucessfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Sucessfully", safe=False)

def grade_api(request, id=0):
    if request.method == 'GET':
        grades = Grades.objects.all()
        grades_serializer = GradeSerializer(grades, many=True)
        return JsonResponse(grades_serializer.data, safe=False)
    elif request.method == 'POST':
        grade_data = JSONParser().parse(request)
        gradess_serializer = GradeSerializer(data=grade_data)
        if grades_serializer.is_valid():
            grades_serializer.save()
            return JsonResponse("Added Sucessfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        grade_data = JSONParser().parse(request)
        grade = Grades.objects.get(
            GradeId=grade_data['GradeId'])
        grades_serializer = GradeSerializer(
            grade, data=grade_data)
        if grades_serializer.is_valid():
            grades_serializer.save()
            return JsonResponse("Updated Sucessfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        grade = Grades.objects.get(GradeId=id)
        grade.delete()
        return JsonResponse("Deleted Sucessfully", safe=False)


@csrf_exempt
def employee_api(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Sucessfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(
            EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(
            employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Sucessfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Sucessfully", safe=False)


@csrf_exempt
def save_file(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
