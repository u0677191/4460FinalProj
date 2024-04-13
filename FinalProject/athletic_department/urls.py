from django.urls import path, include
from . import views
from .views import AthleteCreateView, TeamCreateView , AthleteUpdateView, AthleteDetailView, AthleteDeleteView, employee_login, employee_dashboard


urlpatterns = [

    path('homepage/', views.homepage, name='homepage'),

    path('teams/', views.team_list, name='team_list'),
    path('teams/create/', TeamCreateView.as_view(), name='team_create'),

    
    path('athlete/create/', AthleteCreateView.as_view(), name='athlete_create'),
    path('athlete/update/', AthleteUpdateView.as_view(), name='athlete_update'),
    path('athlete/detail/', AthleteDetailView.as_view(), name='athlete_detail'),
    path('athlete/<int:pk>/delete/', AthleteDeleteView.as_view(), name='athlete_delete'),

    path('employee_login/', views.employee_login, name='employee_login'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),

    #path('add_employee/', views.add_employee, name='add_employee'),

    

    # Define other URLs for CRUD operation
]


