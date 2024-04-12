from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




class Team(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=100)
    email = models.EmailField(default='')
    established_date = models.DateField(default=timezone.now) 

class Employee(models.Model):
    employeeid = models.CharField(max_length=100,default='')
    lastname = models.CharField(max_length=100,default='')
    firstname = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=100,default='Employee')
    address = models.CharField(max_length=255,default='')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    TYPE_CHOICES = (
        ('Salary', 'Salary'),
        ('Hourly', 'Hourly'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Salary')  
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0) 

class Athlete(models.Model):
    athleteid = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    firstname = models.CharField(max_length=100,default='')
    position = models.CharField(max_length=100, default='')
    academic_level = models.CharField(max_length=100, default='')
    contact = models.CharField(max_length=100, default='')
    sport_type= models.CharField(max_length=100,default='')  # Add this field


class Equipment(models.Model):
    equipmentid = models.CharField(max_length=100, null=True)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    annual_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    year = models.PositiveSmallIntegerField(null=True)

class Event(models.Model):
    eventid = models.CharField(max_length=100, default='')
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE, default='')
    venue = models.CharField(max_length=100,default='')
    date = models.DateField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    opponent = models.CharField(max_length=100,default='')

class Rank(models.Model):
    rankid = models.CharField(max_length=100)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    rank = models.IntegerField()
    date = models.DateField()

class Scholarship(models.Model):
    scholarshipid = models.CharField(max_length=100)
    athleteid = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    donor = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class Income(models.Model):
    incomeid = models.CharField(max_length=100)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveSmallIntegerField()

# Remember to run migrations after defining your models
