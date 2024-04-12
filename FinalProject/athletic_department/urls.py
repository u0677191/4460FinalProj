from django.urls import path
from . import views 
from .views import TeamListView, TeamDetailView, TeamCreateView, TeamUpdateView, TeamDeleteView, EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, athletes_by_sport

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),

    path('teams/', TeamListView.as_view(), name='team_list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('teams/create/', TeamCreateView.as_view(), name='team_create'),
    path('teams/<int:pk>/update/', TeamUpdateView.as_view(), name='team_update'),
    path('teams/<int:pk>/delete/', TeamDeleteView.as_view(), name='team_delete'),

    # Employee URLs
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    
    path('athletes/<str:sport_type>/', views.athletes_by_sport, name='athletes_by_sport'),

    # URL patterns for athletes
    path('athletes/', views.AthleteListView.as_view(), name='athlete_list'),
    path('athletes/create/', views.AthleteCreateView.as_view(), name='athlete_create'),
    path('athletes/<int:pk>/', views.AthleteDetailView.as_view(), name='athlete_detail'),
    path('athletes/<int:pk>/update/', views.AthleteUpdateView.as_view(), name='athlete_update'),
    path('athletes/<int:pk>/delete/', views.AthleteDeleteView.as_view(), name='athlete_delete'),

    path('homepage/administrator_login/', views.administrator_login, name='administrator_login'),
    path('administrator_dashboard/', views.administrator_dashboard, name='administrator_dashboard'),
    path('login/', views.administrator_login, name='login_view'),




]