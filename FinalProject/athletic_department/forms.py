from django import forms
from .models import Team, Employee, Athlete, Equipment, Event, Rank, Scholarship, Income

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employeeid', 'lastname', 'firstname', 'title', 'address', 'start_date', 'end_date', 'type', 'cost']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = '__all__'

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class RankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = '__all__'

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        fields = '__all__'

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'


#mic