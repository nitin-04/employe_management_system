from django.shortcuts import render, HttpResponse, redirect
from .models import Employee, Role, Department
from django.db.models import Q

# Create your models here.

# Create your views here.


def index(request):
    return render(request, 'emp.html')


def all(request):
    emp = Employee.objects.all()
    return render(request, 'all.html', {'employee': emp})


def add(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = int(request.POST['department'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone_no = int(request.POST['phone_no'])

        new_emp = Employee(first_name=first_name, last_name=last_name, department_id=department, salary=salary, bonus=bonus, role_id=role,
        phone_no=phone_no)
        new_emp.save()
        dep = Department.objects.all()


        # return HttpResponse("Employee added successfully..........")
        # return redirect("all")
        return render(request, 'all.html', {'department': dep} )

    elif request.method == "GET":
        return render(request, 'add.html')
        # return HttpResponse('An Execption Occured! Employee has not been added..')

    else:
        return HttpResponse("An error occured!...")


def dele(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee delete successfully")
        except:
            return HttpResponse("Please enter a valid employee id")
    emp = Employee.objects.all()
    return render(request, 'dele.html', {'employee': emp})


def filter(request):
    if request.method == 'POST':
        name =          request.POST['name']
        department =    request.POST['department']
        role =          request.POST['role']
        emp =           Employee.objects.all()
        if name:
            emp = emp.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if department:
            emp = emp.filter(department__name__icontains = department)
        if role:
            emp = emp.filter(role__name__icontains = role)


        return render(request, 'all.html', {'employee': emp})

    elif request.method == 'GET':
        return render(request, 'filter.html')
    else:
        return HttpResponse('An Exception Occurred')
    
