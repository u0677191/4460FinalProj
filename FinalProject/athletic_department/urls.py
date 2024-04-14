from django.urls import path, include
from . import views
from .views import (AthleteCreateView, TeamCreateView, TeamUpdateView, TeamDetailView, TeamDeleteView, AthleteUpdateView,
                    AthleteDetailView, AthleteDeleteView, EmployeeCreateView, EmployeeDeleteView, EmployeeUpdateView, EmployeeListView,
                    EmployeeDetailView, EquipmentDeleteView, EquipmentDetailView, EquipmentUpdateView, EquipmentCreateView, athlete_delete, 
                    employee_detail, employee_delete, athlete_list, athlete_detail, employee_create, equipment_detail, equipment_list, 
                    equipment_delete, team_list, team_delete, team_detail, team_create, employee_list, EventCreateView, 
                    EventDeleteView, EventUpdateView, EventDetailView, event_detail, event_list, event_create, event_delete, 
                    )

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
    #old that was working
    path('employee_login/', views.employee_login, name='employee_login'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    #path('employee_list/', views.employee_list, name='employee_list'),
    #path('employee/create/', employee_create, name='employee_create'),
    #path('employee/<str:employeeid>/', employee_detail, name='employee_detail'),
    #path('employee/delete/<str:employeeid>/', employee_delete, name='employee_delete'),

    #new to make work better
    path('employee/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/detail/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee/delete/<str:employeeid>/', employee_delete, name='employee_delete'),
    path('employees/', employee_list, name='employee_list'),
    path('employee/<str:employeeid>/', employee_detail, name='employee_detail'),
    
    # Begin Equipment Paths

    path('equipment/create/', EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/update/', EquipmentUpdateView.as_view(), name='equipment_update'),
    path('equipment/detail/', EquipmentDetailView.as_view(), name='equipment_detail'),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment_delete'),
    path('equipment/delete/<str:athleteid>/', equipment_delete, name='equipment_delete'),
    path('equipments/', equipment_list, name='equipment_list'),
    path('equipment/<str:athleteid>/', equipment_detail, name='equipment_detail'),
    
    # Begin Event Paths

    path('event/create/', EventCreateView.as_view(), name='event_create'),
    path('event/update/', EventUpdateView.as_view(), name='event_update'),
    path('event/detail/', EventDetailView.as_view(), name='event_detail'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('event/delete/<str:eventid>/', event_delete, name='event_delete'),
    path('event/', event_list, name='event_list'),
    path('event/<str:athleteid>/', event_detail, name='event_detail'),
]


