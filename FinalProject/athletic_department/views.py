from django.shortcuts import render
from .models import Team

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'athletic_department/team_list.html', {'teams': teams})

def homepage(request):
    return render(request, 'athletic_department/Homepage.html')
