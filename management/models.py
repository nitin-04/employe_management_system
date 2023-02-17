from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20)
    department = models.ForeignKey(Department,default=0, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,default=0 ,on_delete=models.CASCADE)
    phone_no = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name


    