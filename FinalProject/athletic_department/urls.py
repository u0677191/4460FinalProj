from django.urls import path, include
from . import views
from .views import (AthleteCreateView, TeamCreateView, TeamUpdateView, TeamDetailView, TeamDeleteView, AthleteUpdateView, AthleteDetailView, AthleteDeleteView, 
                    athlete_delete, employee_detail, employee_delete, athlete_list, athlete_detail, employee_create, 
                    team_list, team_delete, team_detail, team_create)

#app_name = 'athletic_department'

urlpatterns = [
    

    path('homepage/', views.homepage, name='homepage'),

    # Begin Team Paths
    path('team/update/', TeamUpdateView.as_view(), name='team_update'),
    path('team/create/', TeamCreateView.as_view(), name='team_create'),
    path('team/detail/', TeamDetailView.as_view(), name='teams_detail'),    
    path('team/<int:pk>/delete/', TeamDeleteView.as_view(), name='team_delete'),    
    path('team/delete/<str:teamid>/', team_delete, name='team_delete'),
    path('team/<str:teamid>/', team_detail, name='team_detail'),
    path('teams/', team_list, name='team_list'),


    # Begin Athlete Paths
    path('athlete/create/', AthleteCreateView.as_view(), name='athlete_create'),
    path('athlete/update/', AthleteUpdateView.as_view(), name='athlete_update'),
    path('athlete/detail/', AthleteDetailView.as_view(), name='athlete_detail'),
    path('athlete/<int:pk>/delete/', AthleteDeleteView.as_view(), name='athlete_delete'),
    path('athlete/delete/<str:athleteid>/', athlete_delete, name='athlete_delete'),
    path('athletes/', athlete_list, name='athlete_list'),
    path('athlete/<str:athleteid>/', athlete_detail, name='athlete_detail'),

    # Begin Employee Paths
    path('employee_login/', views.employee_login, name='employee_login'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee/create/', employee_create, name='employee_create'),
    path('employee/<str:employeeid>/', employee_detail, name='employee_detail'),
    path('employee/delete/<str:employeeid>/', employee_delete, name='employee_delete'),
    
    
    # Define other URLs for CRUD operation
]


