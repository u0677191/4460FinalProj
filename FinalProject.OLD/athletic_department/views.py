from django.shortcuts import render, redirect
from .models import Team, Employee
from django.views.generic import CreateView, UpdateView, DeleteView, ListView


from .forms import TeamForm, EmployeeForm
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
    success_url = '/teams/'
