from django.db import models
from django.core.validators import validate_email
# from django.core.exceptions import ValidationError


class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    Email = models.EmailField(max_length=25, validators=[validate_email], unique=True)
    Pass = models.CharField(max_length=30)
    Name = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Phone = models.CharField(max_length=9)

    # def validatePass():
    #     special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
    #     if not any(char.isdigit() for char in Pass):
    #         raise ValidationError(_('Password must contain at least 1 digit.'))
    #     if not any(char.isalpha() for char in Pass):
    #         raise ValidationError(_('Password must contain at least 1 letter.'))
    #     if not any(char in special_characters for char in Pass):
    #         raise ValidationError(_('Password must contain at least 1 special character.'))


class Visit(models.Model):
    VisitId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey('User', on_delete=models.CASCADE)
    ServiceeId = models.ForeignKey('Servicee', on_delete=models.CASCADE)
    Ddate = models.DateField()
    Hhour = models.TimeField()
    Status = models.CharField(max_length=2)


class Servicee(models.Model):
    ServiceeId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)
    Price = models.IntegerField()
    Time = models.IntegerField()