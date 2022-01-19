from django.db import models
from django.core.validators import validate_email


class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    Email = models.EmailField(max_length=25, validators=[validate_email], unique=True)
    Pass = models.CharField(max_length=30)
    Name = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Phone = models.CharField(max_length=9)

class Servicee(models.Model):
    ServiceeId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)
    Price = models.IntegerField()
    Time = models.IntegerField()

class Visit(models.Model):
    VisitId = models.AutoField(primary_key=True)
    userr = models.ForeignKey(User, on_delete=models.CASCADE)
    servicee = models.ForeignKey(Servicee, on_delete=models.CASCADE, default=1)
    Ddate = models.DateField()
    Hhour = models.TimeField()
    Status = models.CharField(max_length=2)
