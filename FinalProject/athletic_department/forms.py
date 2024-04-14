from django import forms
from django.core.exceptions import ValidationError
from .models import Team, Employee, Athlete, Equipment, Event, Rank, Scholarship, Income

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employeeid', 'firstname', 'lastname', 'title', 'address', 'start_date', 'end_date', 'type', 'cost']

    def clean_employeeid(self):
        employeeid = self.cleaned_data.get('employeeid')
        # Check if the employeeid is already in use and the instance is not the same as the one being updated
        if Employee.objects.filter(employeeid=employeeid).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Employee with this EmployeeID already exists.')
        return employeeid

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
        
