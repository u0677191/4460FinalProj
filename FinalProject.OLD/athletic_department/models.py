from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=100)
    email = models.EmailField()
    established_date = models.DateField()

class Employee(models.Model):
    employeeid = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    TYPE_CHOICES = (
        ('Salary', 'Salary'),
        ('Hourly', 'Hourly'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class Athlete(models.Model):
    athleteid = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    academic_level = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

class Equipment(models.Model):
    equipmentid = models.CharField(max_length=100)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    annual_cost = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveSmallIntegerField()

class Event(models.Model):
    eventid = models.CharField(max_length=100)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    income = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    opponent = models.CharField(max_length=100)

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



