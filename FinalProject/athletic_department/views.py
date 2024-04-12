from django.shortcuts import render, redirect
from .models import Team, Employee, Athlete

from django.views import View
from .forms import TeamForm, EmployeeForm,AthleteForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.views.generic import FormView

def homepage(request):
    return render(request, 'athletic_department/homepage.html')


class TeamListView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'athletic_department/team_list.html', {'teams': teams})

class TeamDetailView(View):
    def get(self, request, pk):
        team = Team.objects.get(pk=pk)
        return render(request, 'athletic_department/team_detail.html', {'team': team})

class TeamCreateView(View):
    def get(self, request):
        form = TeamForm()
        return render(request, 'athletic_department/team_create.html', {'form': form})
    
    def post(self, request):
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')  
        return render(request, 'athletic_department/team_create.html', {'form': form})

class TeamUpdateView(View):
    def get(self, request, pk):
        team = Team.objects.get(pk=pk)
        form = TeamForm(instance=team)
        return render(request, 'athletic_department/team_update.html', {'form': form})

    def post(self, request, pk):
        team = Team.objects.get(pk=pk)
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
        return render(request, 'athletic_department/team_update.html', {'form': form})

class TeamDeleteView(View):
    def get(self, request, pk):
        team = Team.objects.get(pk=pk)
        return render(request, 'athletic_department/team_delete.html', {'team': team})

    def post(self, request, pk):
        team = Team.objects.get(pk=pk)
        team.delete()
        return redirect('team_list')
    
class EmployeeListView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'athletic_department/employee_list.html', {'employees': employees})
    
class EmployeeCreateView(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'athletic_department/employee_create.html', {'form': form})
    
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  
        return render(request, 'athletic_department/employee_create.html', {'form': form})

class EmployeeUpdateView(View):
    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        form = EmployeeForm(instance=employee)
        return render(request, 'athletic_department/employee_update.html', {'form': form})
        
class EmployeeDeleteView(View):
    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        return render(request, 'athletic_department/employee_delete.html', {'employee': employee})

    def post(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return redirect('employee_list')
    
def athletes_by_sport(request, sport_type):
    athletes = Athlete.objects.filter(sport_type=sport_type)
    return render(request, 'athletic_department/athletes_by_sport.html', {'athletes': athletes, 'sport_type': sport_type})


class AthleteListView(View):
    def get(self, request):
        athletes = Athlete.objects.all()
        return render(request, 'athletic_department/athlete_list.html', {'athletes': athletes})

class AthleteCreateView(View):
    def get(self, request):
        form = AthleteForm()
        return render(request, 'athletic_department/athlete_create.html', {'form': form})
    
    def post(self, request):
        form = AthleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('athlete_list')  # Redirect to the athlete list after successful creation
        return render(request, 'athletic_department/athlete_create.html', {'form': form})

class AthleteDetailView(View):
    def get(self, request, pk):
        athlete = Athlete.objects.get(pk=pk)
        return render(request, 'athletic_department/athlete_detail.html', {'athlete': athlete})

class AthleteUpdateView(View):
    def get(self, request):
        athlete = Athlete.objects.get
        form = AthleteForm(instance=athlete)
        return render(request, 'athletic_department/athlete_update.html', {'form': form})

    def post(self, request):
        athlete = Athlete.objects.get
        form = AthleteForm(request.POST, instance=athlete)
        if form.is_valid():
            form.save()
            return redirect('athlete_list')
        return render(request, 'athletic_department/athlete_update.html', {'form': form})
    
class AthleteDeleteView(View):
    def get(self, request):
        athlete = Athlete.objects.get
        return render(request, 'athletic_department/athlete_delete.html', {'athlete': athlete})

    def post(self, request):
        athlete = Athlete.objects.get
        athlete.delete()
        return redirect('athlete_list')
