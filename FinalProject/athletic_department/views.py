from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Team, Employee , Athlete
from django.views.generic import CreateView, UpdateView, DeleteView, ListView , DetailView
from .forms import TeamForm, EmployeeForm, AthleteForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def homepage(request):
    return render(request, 'athletic_department/Homepage.html')

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'athletic_department/team_list.html', {'teams': teams})



class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'athletic_department/team_form.html'
    success_url = '/teams/'

class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'athletic_department/team_form.html'
    success_url = '/teams/'

class TeamDeleteView(DeleteView):
    model = Team
    form_class = TeamForm
    template_name = 'athletic_department/team_form.html'
    success_url = '/teams/'

class AthleteListView(ListView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athletic_department/athlete_form.html'
    success_url = '/athletes/'

class AthleteCreateView(CreateView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athletic_department/athlete_create.html'
    success_url = '/athletes/'

class AthleteUpdateView(UpdateView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athletic_department/athlete_update.html'
    success_url = '/athletes/'

class AthleteDetailView(DetailView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athletic_department/athlete_detail.html'
    success_url = '/athletes/'

class AthleteDeleteView(DeleteView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athletic_department/athlete_delete.html'
    success_url = '/athletes/'

#def employee_login(request):
   # return render(request, 'athletic_department/employee_login.html')

def employee_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_dashboard')  # Redirects to the employee dashboard
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'athletic_department/employee_login.html')

def employee_dashboard(request):
    return render(request, 'athletic_department/employee_dashboard.html')