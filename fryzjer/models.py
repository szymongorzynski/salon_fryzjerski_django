from django.db import models
from django.core.validators import validate_email
# from django.core.exceptions import ValidationError


class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    Email = models.EmailField(max_length=25, validators=[validate_email], unique=True)
    Pass = models.CharField(max_length=30)

class Customer(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    UserId = models.IntegerField(default=None)
    Name = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Phone = models.CharField(max_length=9, unique=True)

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    Userr = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Pesel = models.CharField(max_length=25)
    Town = models.CharField(max_length=25)
    HouseNumber = models.CharField(max_length=25)
    Salary = models.FloatField()
    Phone = models.CharField(max_length=9)

class Servicee(models.Model):
    ServiceeId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)
    Price = models.IntegerField()
    Time = models.IntegerField()

class Discount(models.Model):
    DiscountId = models.AutoField(primary_key=True)
    Percent = models.FloatField()
    VisitCount = models.IntegerField()

class Visit(models.Model):
    VisitId = models.AutoField(primary_key=True)
    Customerr = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    servicee = models.ForeignKey(Servicee, on_delete=models.CASCADE, default=1)
    Employeee= models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    DiscountId = models.IntegerField(default=None)
    Ddate = models.DateField()
    Hhour = models.TimeField()
    Status = models.CharField(max_length=2)